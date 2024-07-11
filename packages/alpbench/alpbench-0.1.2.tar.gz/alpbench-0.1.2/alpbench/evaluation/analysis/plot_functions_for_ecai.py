import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize, LinearSegmentedColormap

import pandas as pd
from py_experimenter.experimenter import PyExperimenter
import json
import os
from scipy.stats import ttest_ind_from_stats
from scipy.stats import ttest_ind as tt



class BudgetPerformancePlot:
    """BudgetPerformancePlot

    This class plots the performance of different sampling strategies over the budget.

    Args:
        data (dict): The data to plot.
        path_to_save (str): The path to save the plot.

    Attributes:
        data (dict): The data to plot.
        path_to_save (str): The path to save the plot.

    """
    def __init__(self, df, openml_id, learner_name, metric, path_to_save=None):
        self.df = df
        self.openml_id = openml_id
        self.learner_name = learner_name
        self.metric = metric
        self.path_to_save = path_to_save
        self.plot_data = None

    def generate_plot_data(self):
        """
        This function generates the data to plot.
        """
        # get data for openml_id
        df = self.df[self.df['openml_id'] == self.openml_id]
        # get data for learner
        df = df[df['learner_name'] == self.learner_name]
        # get unique query strategy names
        query_strategies = df['query_strategy_name'].unique()
        # get unique budget values
        budgets = df['len_X_l'].unique()

        # create dict to store data
        data = {}
        for qs in query_strategies:
            data[qs] = {'budget': [], 'mean': [], 'std': [], 'mean_top': [], 'std_top': [], 'mean_low': [], 'std_low': [], 'accs_iter_3': {},'accs_iter_1': {},'accs_iter_2': {}, 'accs_iter_8': {}, 'accs_iter_20': {}, 'accs_iter_init': {}}
            for enum,budget in enumerate(budgets):
                # get data for query strategy and budget
                df_temp = df[(df['query_strategy_name'] == qs) & (df['len_X_l'] == budget)]

                #print("DF TEMP", df_temp)
                #return


                # reset index
                df_temp.reset_index()
                # get mean and std of metric
                mean = df_temp[self.metric].mean()
                std = df_temp[self.metric].std()
                # get ids of top 5 and low 5 values
                if enum == 0:
                    mean_top_ids = df_temp[self.metric].argsort().tolist()[-10:]
                    mean_low_ids = df_temp[self.metric].argsort().tolist()[:10]
                    data[qs]['accs_iter_init']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_init']['weak'] = df_temp[self.metric].values[mean_low_ids]
                if enum == 1:
                    data[qs]['accs_iter_1']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_1']['weak'] = df_temp[self.metric].values[mean_low_ids]
                if enum == 2:
                    data[qs]['accs_iter_2']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_2']['weak'] = df_temp[self.metric].values[mean_low_ids]
                if enum == 3:
                    data[qs]['accs_iter_3']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_3']['weak'] = df_temp[self.metric].values[mean_low_ids]
                if enum == 8:
                    data[qs]['accs_iter_8']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_8']['weak'] = df_temp[self.metric].values[mean_low_ids]
                if enum == 20:
                    data[qs]['accs_iter_20']['strong'] = df_temp[self.metric].values[mean_top_ids]
                    data[qs]['accs_iter_20']['weak'] = df_temp[self.metric].values[mean_low_ids]

                df_reset = df_temp[self.metric].reset_index()
                mean_top = np.array(df_reset.loc[mean_top_ids][self.metric]).mean()
                mean_low = np.array(df_reset.loc[mean_low_ids][self.metric]).mean()
                std_top = np.array(df_reset.loc[mean_top_ids][self.metric]).std()
                std_low = np.array(df_reset.loc[mean_low_ids][self.metric]).std()

                # append data to dict
                data[qs]['budget'].append(budget)
                data[qs]['mean'].append(mean)
                data[qs]['std'].append(std)
                data[qs]['mean_top'].append(mean_top)
                data[qs]['std_top'].append(std_top)
                data[qs]['mean_low'].append(mean_low)
                data[qs]['std_low'].append(std_low)


        self.plot_data = data


    def show(self):
        """
        This function plots the performance of different query strategies over the budget and saves
        it as .pdf under the specified path.
        """
        data = self.plot_data
        if len(data.keys()) == 0:
            return
        else:
            oid = self.openml_id
            # we want to order the QS by grouping them into categories, also each category gets a different
            # color coding (uncertainty based are redish, representative are greenish, hybrid are blueish,
            # random is pink)
            keys = data.keys()
            list_of_qs = list(keys)
            all_qs_ordered = ["random", "entropy", "least_confident", "margin", "power_margin",
                        "max_entropy", "bald", "power_bald", "qbc_variance_ratio",
                        "kmeans", "core_set","typ_cluster",
                        "cluster_margin", "falcun",  "weighted_cluster"]
            # order the query strategies
            ordered_qs = []
            for qs in all_qs_ordered:
                if qs in list_of_qs:
                    ordered_qs.append(qs)

            fig, ax = plt.subplots(1)
            # colormap of len(keys)
            colors = plt.cm.tab20(np.linspace(0, 1, len(keys)))
            color_dict = {"random": "magenta", "least_confident": "rosybrown", "margin": "red",
                          "entropy": "orange", "power_margin": "brown", "bald": "tomato",
                          "power_bald": "coral", "max_entropy": "sandybrown", "qbc_variance_ratio": "peachpuff",
                          "core_set": "limegreen", "typ_cluster": "forestgreen", "cluster_margin": "mediumblue",
                          "weighted_cluster": "turquoise", "falcun": "blue"}
            for cl, key in enumerate(ordered_qs):
                budget = np.array(data[key]['budget'])
                mu = np.array(data[key]['mean'])
                std = np.array(data[key]['std'])/np.sqrt(10)
                mu_top = np.array(data[key]['mean_top'])
                std_top = np.array(data[key]['std_top'])/np.sqrt(10)
                mu_low = np.array(data[key]['mean_low'])
                std_low = np.array(data[key]['std_low'])/np.sqrt(10)
                qs = key
                cl = color_dict[qs]
                #plt.plot(budget, mu, lw=2, label=key, color=cl)
                #plt.fill_between(budget, mu+std, mu-std,  facecolor=cl, alpha=0.5)
                #plt.plot(budget, mu_top, lw=2, label=key, color=cl)
                #plt.plot(budget, mu_low, lw=2,  color=cl, linestyle='--')
                plt.fill_between(budget, mu_top+std_top, mu_top-std_top,  facecolor=cl, alpha=0.5)
                plt.fill_between(budget, mu_low+std_low, mu_low-std_low,  facecolor=cl, alpha=0.5)
            for cl, key in enumerate(ordered_qs):
                budget = np.array(data[key]['budget'])
                mu = np.array(data[key]['mean'])
                std = np.array(data[key]['std'])/np.sqrt(10)
                mu_top = np.array(data[key]['mean_top'])
                std_top = np.array(data[key]['std_top'])/np.sqrt(10)
                mu_low = np.array(data[key]['mean_low'])
                std_low = np.array(data[key]['std_low'])/np.sqrt(10)
                qs = key
                cl = color_dict[qs]
                #plt.plot(budget, mu, lw=2, label=key, color=cl)
                #plt.fill_between(budget, mu+std, mu-std,  facecolor=cl, alpha=0.5)
                plt.plot(budget, mu_top, lw=2, label=key, color=cl)
                plt.plot(budget, mu_low, lw=2,  color=cl, linestyle='--')
                #plt.fill_between(budget, mu_top+std_top, mu_top-std_top,  facecolor=cl, alpha=0.5)
                #plt.fill_between(budget, mu_low+std_low, mu_low-std_low,  facecolor=cl, alpha=0.5)

            qs_for_figure = {"margin": "MS", "least_confident": "LC", "entropy": "ES",
                                "power_margin": "PowMS", "bald": "BALD", "power_bald": "PowBALD",
                                "max_entropy": "MaxEnt", "qbc_variance_ratio": "QBC VR",
                                "core_set": "CoreSet", "typ_cluster": "TypClu", "cluster_margin": "CluMS",
                                "weighted_cluster": "Clue", "falcun": "FALCUN", "random": "Rand"}
            learner_for_figure = {"knn_3": "KNN", "svm_rbf": "SVM", "mlp": "MLP", "rf_entropy": "RF",
                                    "catboost": "Catboost", "xgb": "XGB", "tabnet": "Tabnet", "tabpfn": "TabPFN"}

            handles, labels = plt.gca().get_legend_handles_labels()

            new_labels = []
            for label in labels:
                new_labels.append(qs_for_figure[label])

            plt.title(learner_for_figure[self.learner_name] + " on id " + str(self.openml_id), fontsize=30)
            plt.legend(handles, new_labels, fontsize=20, loc='lower right')# fontsize=25,loc='center left', bbox_to_anchor=(1, 0.5))
            plt.yticks(fontsize=20)
            plt.xticks(fontsize=20)
            ax.set_xlabel('Number of labeled instances', fontsize=25)
            ax.set_ylabel('test accuracy', fontsize=25)
            [l.set_visible(False) for (i, l) in enumerate(ax.xaxis.get_ticklabels()) if i % 2 != 0]

            # save image
            if self.path_to_save is not None:
                if not os.path.exists(self.path_to_save):
                    os.makedirs(self.path_to_save)
            else:
                self.path_to_save = "FIGURES/BUDGET_PERFORMANCE_PLOT/" +  str(self.openml_id) + "/"
                if not os.path.exists(self.path_to_save):
                    os.makedirs(self.path_to_save)
            self.path_to_save = self.path_to_save + str(self.learner_name) + ".pdf"
            fig.savefig(self.path_to_save, facecolor='white', transparent=True, bbox_inches='tight')
            plt.close()



class HeatMapPlot:
    """HeatMapPlot

    This class plots a heatmap of the performance of different active learning pipelines as well as win or lose-
    matrices for the specified learner comparing different query strategies.

    Args:
        data (dict): The data to plot.
        path_to_save (str): The path to save the plot.
        filter_ids (str): The filter ids.
        take_statistical_insignificant (bool): Whether to take statistical insignificant values.

    Attributes:
        data (dict): The data to plot.
        path_to_save (str): The path to save the plot.
        filter_ids (str): The filter ids.
        take_statistical_insignificant (bool): Whether to take statistical insignificant values.

    """
    def __init__(self, df, learner_name, path_to_save = None, filter_ids = "all", take_statistical_insignificant=False):
        self.df = df
        self.path_to_save = path_to_save
        self.filter_ids = filter_ids
        self.take_statistical_insignificant = take_statistical_insignificant


    def show_heatmap(self):
        """
        This function plots heatmaps to compare performances of different active learning pipelines.
        The figures are saved under the specified path.
        """
        learners_ordered = ["knn_3", "svm_rbf", "rf_entropy", "catboost",
                            "xgb","mlp",
                            "tabnet",
                            "tabpfn"]
        info = ["margin", "entropy", "power_margin",  "power_bald"]
        repr = ["core_set", "typ_cluster"]
        hybr = ["cluster_margin", "falcun"]

        sampling_strategies_ordered = ["random",
                                       "margin",
                                       # "least_confident",
                                       "entropy", #"qbc_variance_ratio",
                                       #"max_entropy",
                                       "power_margin", #"bald",
                                       "power_bald",
                                       "core_set", #"kmeans",
                                       "typ_cluster",
                                       "cluster_margin",
                                       #"weighted_cluster",
                                       "falcun"
                                       ]



        learners = self.data['learners']
        sampling_strategies = self.data['sampling_strategies']
        heatmap = self.data['heatmap']


        res = np.zeros((len(learners_ordered), len(sampling_strategies_ordered)))
        for enum_i, l in enumerate(learners_ordered):
            for enum_j, qs in enumerate(sampling_strategies_ordered):
                res[enum_i, enum_j] = heatmap[(l,qs)]


        setting_name = self.data['setting_name']
        metric_name = self.data['metric_name'] + "_AUBC"


        # Define a custom colormap from light red to red
        light_red_to_red = LinearSegmentedColormap.from_list('light_red_to_red', ['lavender', 'darkblue'])
        greens = plt.cm.Greens
        reds = plt.cm.Reds
        blues = plt.cm.Blues
        purples = plt.cm.Purples

        # Normalize the data
        norm = Normalize(vmin=res.min(), vmax=res.max())

        # Apply the custom colormap to the data
        colors = light_red_to_red(norm(res))
        red_colors = reds(norm(res))
        green_colors = greens(norm(res))
        blue_colors = blues(norm(res))
        purple_colors = purples(norm(res))



        # Erstellen des Plots
        fig, ax = plt.subplots(figsize=(1.5 * len(sampling_strategies_ordered), 1.5 * len(learners_ordered)))

        # Zeichnen der Tafel mit den Farben basierend auf den Werten
        for i,l in enumerate(learners_ordered):
            for j,qs in enumerate(sampling_strategies_ordered):
                #print("hey", str(int(res_wins[i,j])) + "/" + str(int(res_losses[i,j])))
                #print("total " , int(res_wins[i,j] + res_losses[i,j]))
                ax.text(j + 0.5, i + 0.5, str(int(res[i,j])), ha='center', va='center', color='white',
                        fontsize=30,
                        weight='bold')
                if qs in info:
                    colors = red_colors
                elif qs in repr:
                    colors = green_colors
                elif qs in hybr:
                    colors = blue_colors
                else:
                    colors = purple_colors
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color=colors[i, j]))

        # Einstellungen für den Plot
        x_pos = np.arange(1, len(sampling_strategies_ordered) + 1.5, 1) - .5
        y_pos = np.arange(1, len(learners_ordered) + 1.5, 1) - .5


        x_pos[-1] -= .5
        y_pos[-1] -= .5

        ax.set_xticks(x_pos)
        ax.set_yticks(y_pos)

        learners_ordered = ["KNN", "SVM",  "RF", "Catboost", "XGB","MLP",
                            "Tabnet",
                            "TabPFN"]
        sampling_strategies_ordered = ["Rand",
                                       "MS", #"least_confident",
                                       "ES",  # "qbc_variance_ratio",
                                       # "max_entropy",
                                       "PowMS",  # "bald",
                                       "PowBALD",
                                       "CoreSet",
                                       "TypClu",
                                       # "kmeans",
                                       "CluMS",
                                       # "weighted_cluster",
                                       "FALCUN"
                                       ]

        sampling_names = list(sampling_strategies_ordered)
        learners_names = list(learners_ordered)

        sampling_names.append(" ")
        learners_names.append(" ")
        ax.set_xticklabels(sampling_names, fontsize=40, rotation=45)
        ax.set_yticklabels(learners_names, fontsize=40)
        if self.take_statistical_insignificant:
            fig.suptitle("Setting: " + setting_name + ", Datasets: " + str(self.filter_ids),
                     fontsize=50)
            ax.set_title("(statistically significant)", fontsize=30)

        else:
            fig.suptitle("Setting: " + setting_name + ", Datasets: " + str(self.filter_ids),
                     fontsize=50)
            ax.set_title("(not statistically significant)", fontsize=30)#, color='white')

        filter_ids = self.data['filter_ids']
        if self.path_to_save is not None:
            PATH = self.path_to_save + str(filter_ids) +"/"
            if not os.path.exists(PATH):
                os.makedirs(PATH)
            SAVE_PATH = PATH + setting_name +  metric_name +  "_"+str(filter_ids) +"_.pdf"
        print("saved in ", SAVE_PATH)
        fig.savefig(SAVE_PATH, facecolor='white', transparent=True, bbox_inches='tight')
        #plt.show()



class WinMatrixPlot:
    def __init__(self, df, learner_name, path_to_save = None, filter_ids = "all", take_statistical_insignificant=False):
        self.df = df
        self.learner_name = learner_name
        self.path_to_save = path_to_save
        self.filter_ids = filter_ids
        self.take_statistical_insignificant = take_statistical_insignificant

    def generate_win_matrix(self):
        """
        This function generates win-matrices to compare performances of different query strategies combined
        with one fixed learning algorithm.
        """
        df = self.df[self.df['learner_name'] == self.learner_name]
        win_matrix = {}
        query_strategies = self.df['query_strategy_name'].unique()
        for qs1 in query_strategies:
            for qs2 in query_strategies:
                win_matrix[(qs1, qs2)] = [0, 0]

        for oid in df['openml_id'].unique():
            df = df[df['learner_name'] == self.learner_name]
            for qs1 in query_strategies:
                for qs2 in query_strategies:
                    df1 = df[df['query_strategy_name'] == qs1]
                    df2 = df[df['query_strategy_name'] == qs2]
                    mean1 = df1['test_accuracy'].mean()
                    mean2 = df2['test_accuracy'].mean()
                    std1 = df1['test_accuracy'].std()
                    std2 = df2['test_accuracy'].std()
                    t, p = ttest_ind_from_stats(mean1, std1, len(df1), mean2, std2, len(df2))
                    if p < 0.05:
                        if mean1 > mean2:
                            win_matrix[(qs1, qs2)][0] += 1
                        else:
                            win_matrix[(qs1, qs2)][1] += 1





    def show(self):
        """
        This function generates win-matrices to compare performances of different query strategies combined
        with one fixed learning algorithm.
        """

        all_qs_ordered = ["random", "entropy", "least_confident", "margin", "power_margin",
                          "max_entropy", "bald", "power_bald", "qbc_variance_ratio",
                          "kmeans", "core_set", "typ_cluster",
                          "cluster_margin", "falcun", "weighted_cluster"]

        learners_ordered = ["knn_3", "svm_rbf", "mlp","rf_entropy","catboost", "xgb",
        "tabnet", "tabpfn"]

        filter_ids = self.filter_ids




        win_matrix = self.data['learner'][learner]
        print("WIN MATRIX",win_matrix)
        sampling_strategies = win_matrix.keys()


        # create numpy array from dict
        res_wins = np.zeros((len(sampling_strategies_ordered), len(sampling_strategies_ordered)))
        res_losses  = np.zeros((len(sampling_strategies_ordered), len(sampling_strategies_ordered)))

        for i, strat_1 in enumerate(sampling_strategies_ordered):
            for j, strat_2 in enumerate(sampling_strategies_ordered):
                key = ((learner, strat_1), (learner, strat_2))

                # check if key exists in win_matrix
                if key in win_matrix.keys():
                    wins = win_matrix[key][0]
                    losses = win_matrix[key][1]
                else:
                    wins = 0
                    losses = 0
                if i == j:
                    wins = 0
                    losses = 0

                res_wins[i, j] = wins
                res_losses[i, j] = losses


        res_total = np.ones((len(sampling_strategies_ordered), len(sampling_strategies_ordered))) * self.data['num_dataset_ids']
        # set diag to 0
        np.fill_diagonal(res_total, 0)


        setting_name = self.data['setting_name']
        metric_name =  self.data['metric_name'] + "_AUBC"


        light_red_to_red = LinearSegmentedColormap.from_list('light_red_to_red', ['lavender', 'darkblue'])

        greens = plt.cm.Greens
        reds = plt.cm.Reds
        blues = plt.cm.Blues
        purples = plt.cm.Purples


        # Normalize the data
        norm = Normalize(vmin=res_wins.min(), vmax=res_wins.max())

        # Apply the custom colormap to the data
        colors = light_red_to_red(norm(res_wins))

        # Apply the custom colormap to the data
        colors = light_red_to_red(norm(res_wins))
        red_colors = reds(norm(res_wins))
        green_colors = greens(norm(res_wins))
        blue_colors = blues(norm(res_wins))
        purple_colors = purples(norm(res_wins))

        #norm = Normalize(res_wins.min(), vmax=res_wins.max() * 1.5)
        #colors = plt.cm.viridis(norm(res_wins))
        #colors = plt.cm.Reds(norm(res_wins))
        #print("COOLS",colors)
        # Use the 'Reds' colormap for red tones
        #colors = plt.cm.Reds(norm(res_wins))

        # Erstellen des Plots
        fig, ax = plt.subplots(figsize=(1.5 * len(sampling_strategies_ordered), 1.5 * len(sampling_strategies_ordered)))

        # Zeichnen der Tafel mit den Farben basierend auf den Werten
        for i,l in enumerate(sampling_strategies_ordered):
            for j,qs in enumerate(sampling_strategies_ordered):
                #print("hey", str(int(res_wins[i,j])) + "/" + str(int(res_losses[i,j])))
                #print("total " , int(res_wins[i,j] + res_losses[i,j]))

                ax.text(j + 0.5, i + 0.5,
                        str(int(res_wins[i, j])) + "/" + str(int(res_total[i, j])),
                        ha='center', va='center', color='white',
                        fontsize=25,
                        weight='bold')
                if l in info:
                    colors = red_colors
                elif l in repr:
                    colors = green_colors
                elif l in hybr:
                    colors = blue_colors
                else:
                    colors = purple_colors

                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color=colors[i, j]))

        # Einstellungen für den Plot
        x_pos = np.arange(1, len(sampling_strategies_ordered) + 1.5, 1) - .5
        y_pos = np.arange(1, len(sampling_strategies_ordered) + 1.5, 1) - .5


        x_pos[-1] -= .5
        y_pos[-1] -= .5
        print("x_pos", x_pos)
        print("y_pos", y_pos)

        ax.set_xticks(x_pos)
        ax.set_yticks(y_pos)

        sampling_names = ["Rand", "MS", "ES", "PowMS", "PowBALD", "CoreSet", "TypClu", "CluMS", "FALCUN"]
                          # "LC",
                          #"ES",  #"QBC",
                                      # "MaxEnt",
                          #"PowMS", #"BALD",
                          #"PowBALD",
                          # "CoreSet",
                          #"KMeans",
                          #"CluMS",
                          #"TypClu"#,"CLUE",
                          #"FALCUN"
                          #]
        #sampling_names = list(sampling_strategies_ordered)
        learners_names = list(learners)

        sampling_names.append(" ")

        learners_ordered = ["knn_3", "svm_rbf", "mlp", "rf_entropy", "catboost", "xgb",
                            "tabnet", "tabpfn"]

        if learner == "knn_3":
            learner_name = "KNN"
        elif learner == "svm_rbf":
            learner_name = "SVM"
        elif learner == "mlp":
            learner_name = "MLP"
        elif learner == "rf_entropy":
            learner_name = "RF"
        elif learner == "catboost":
            learner_name = "Catboost"
        elif learner == "xgb":
            learner_name = "XGB"
        elif learner == "tabnet":
            learner_name = "Tabnet"
        elif learner == "tabpfn":
            learner_name = "TabPFN"


        learners_names.append(" ")
        ax.set_xticklabels(sampling_names, fontsize=40, rotation=45)
        ax.set_yticklabels(sampling_names, fontsize=40)
        ax.set_title("Setting: " + setting_name + ", Learner: " + learner_name,
                     fontsize=50)
        SAVE_PATH = "fig .pdf"


        if self.path_to_save is not None:
            PATH = self.path_to_save + "/" + str(filter_ids) +"/"
            if not os.path.exists(PATH):
                os.makedirs(PATH)
            SAVE_PATH = PATH + setting_name +  metric_name + "_"+str(learner) + ".pdf"
            print("SAVE PATH", SAVE_PATH)
            fig.savefig(SAVE_PATH, facecolor='white', transparent=True, bbox_inches='tight')
        #plt.show()






class WinMatrixPlot:
    """WinMatrixPlot

    This class plots the win-matrix to compare performances of different query strategies combined with one fixed
    learning algorithm.

    Args:
        df (pd.DataFrame): The dataframe with the computed final AUBC per pipeline.
        learner_name (str): The fixed learner name to generate the win-matrix for.
        path_to_save (str): The path to save the plot.
        take_statistical_insignificant (bool): If True, statistical insignificant results are also considered.

    Attributes:
        df (pd.DataFrame): The dataframe with the computed final AUBC per pipeline.
        learner_name (str): The fixed learner name to generate the win-matrix for.
        path_to_save (str): The path to save the plot.
        take_statistical_insignificant (bool): If True, statistical insignificant results are also considered.
        win_matrix (dict): The win-matrix to compare performances of different query strategies combined with one fixed
        learning algorithm.

    """
    def __init__(self, df, learner_name, path_to_save = None, take_statistical_insignificant=False):
        self.df = df
        self.learner_name = learner_name
        self.path_to_save = path_to_save
        self.take_statistical_insignificant = take_statistical_insignificant
        self.win_matrix = None

    def generate_win_matrix(self):
        """
        This function generates win-matrices to compare performances of different query strategies combined
        with one fixed learning algorithm.
        """
        df = self.df[self.df['learner_name'] == self.learner_name]
        win_matrix = {}
        query_strategies = self.df['query_strategy_name'].unique()
        for qs1 in query_strategies:
            for qs2 in query_strategies:
                win_matrix[(qs1, qs2)] = [0, 0]

        for oid in df['openml_id'].unique():
            df = df[df['learner_name'] == self.learner_name]
            for qs1 in query_strategies:
                for qs2 in query_strategies:
                    df1 = df[df['query_strategy_name'] == qs1]
                    df2 = df[df['query_strategy_name'] == qs2]
                    mean1 = df1['aubc'].mean()
                    mean2 = df2['aubc'].mean()
                    std1 = df1['aubc'].std()
                    std2 = df2['aubc'].std()
                    t, p = ttest_ind_from_stats(mean1, std1, len(df1), mean2, std2, len(df2))
                    if not self.take_statistical_insignificant and p < 0.05:
                        if mean1 > mean2:
                            win_matrix[(qs1, qs2)][0] += 1
                        else:
                            win_matrix[(qs1, qs2)][1] += 1
                    if self.take_statistical_insignificant:
                        if mean1 > mean2:
                            win_matrix[(qs1, qs2)][0] += 1
                        else:
                            win_matrix[(qs1, qs2)][1] += 1
            self.win_matrix = win_matrix
            return win_matrix


    def show(self):
        """
        This function generates win-matrices to compare performances of different query strategies combined
        with one fixed learning algorithm.
        """

        all_qs_ordered = ["random", "entropy", "least_confident", "margin", "power_margin",
                          "max_entropy", "bald", "power_bald", "qbc_variance_ratio",
                          "kmeans", "core_set", "typ_cluster",
                          "cluster_margin", "falcun", "weighted_cluster"]

        learners_ordered = ["knn_3", "svm_rbf", "mlp","rf_entropy","catboost", "xgb",
        "tabnet", "tabpfn"]

        # TODO implement this function bla

        query_strategies = self.win_matrix.keys()


        # create numpy array from dict
        res_wins = np.zeros((len(sampling_strategies_ordered), len(sampling_strategies_ordered)))
        res_losses  = np.zeros((len(sampling_strategies_ordered), len(sampling_strategies_ordered)))

        for i, strat_1 in enumerate(sampling_strategies_ordered):
            for j, strat_2 in enumerate(sampling_strategies_ordered):
                key = ((learner, strat_1), (learner, strat_2))

                # check if key exists in win_matrix
                if key in win_matrix.keys():
                    wins = win_matrix[key][0]
                    losses = win_matrix[key][1]
                else:
                    wins = 0
                    losses = 0
                if i == j:
                    wins = 0
                    losses = 0

                res_wins[i, j] = wins
                res_losses[i, j] = losses


        res_total = np.ones((len(sampling_strategies_ordered), len(sampling_strategies_ordered))) * self.data['num_dataset_ids']
        # set diag to 0
        np.fill_diagonal(res_total, 0)


        setting_name = self.data['setting_name']
        metric_name =  self.data['metric_name'] + "_AUBC"


        light_red_to_red = LinearSegmentedColormap.from_list('light_red_to_red', ['lavender', 'darkblue'])

        greens = plt.cm.Greens
        reds = plt.cm.Reds
        blues = plt.cm.Blues
        purples = plt.cm.Purples


        # Normalize the data
        norm = Normalize(vmin=res_wins.min(), vmax=res_wins.max())

        # Apply the custom colormap to the data
        colors = light_red_to_red(norm(res_wins))

        # Apply the custom colormap to the data
        colors = light_red_to_red(norm(res_wins))
        red_colors = reds(norm(res_wins))
        green_colors = greens(norm(res_wins))
        blue_colors = blues(norm(res_wins))
        purple_colors = purples(norm(res_wins))

        #norm = Normalize(res_wins.min(), vmax=res_wins.max() * 1.5)
        #colors = plt.cm.viridis(norm(res_wins))
        #colors = plt.cm.Reds(norm(res_wins))
        #print("COOLS",colors)
        # Use the 'Reds' colormap for red tones
        #colors = plt.cm.Reds(norm(res_wins))

        # Erstellen des Plots
        fig, ax = plt.subplots(figsize=(1.5 * len(sampling_strategies_ordered), 1.5 * len(sampling_strategies_ordered)))

        # Zeichnen der Tafel mit den Farben basierend auf den Werten
        for i,l in enumerate(sampling_strategies_ordered):
            for j,qs in enumerate(sampling_strategies_ordered):
                #print("hey", str(int(res_wins[i,j])) + "/" + str(int(res_losses[i,j])))
                #print("total " , int(res_wins[i,j] + res_losses[i,j]))

                ax.text(j + 0.5, i + 0.5,
                        str(int(res_wins[i, j])) + "/" + str(int(res_total[i, j])),
                        ha='center', va='center', color='white',
                        fontsize=25,
                        weight='bold')
                if l in info:
                    colors = red_colors
                elif l in repr:
                    colors = green_colors
                elif l in hybr:
                    colors = blue_colors
                else:
                    colors = purple_colors

                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color=colors[i, j]))

        # Einstellungen für den Plot
        x_pos = np.arange(1, len(sampling_strategies_ordered) + 1.5, 1) - .5
        y_pos = np.arange(1, len(sampling_strategies_ordered) + 1.5, 1) - .5


        x_pos[-1] -= .5
        y_pos[-1] -= .5
        print("x_pos", x_pos)
        print("y_pos", y_pos)

        ax.set_xticks(x_pos)
        ax.set_yticks(y_pos)

        sampling_names = ["Rand", "MS", "ES", "PowMS", "PowBALD", "CoreSet", "TypClu", "CluMS", "FALCUN"]
                          # "LC",
                          #"ES",  #"QBC",
                                      # "MaxEnt",
                          #"PowMS", #"BALD",
                          #"PowBALD",
                          # "CoreSet",
                          #"KMeans",
                          #"CluMS",
                          #"TypClu"#,"CLUE",
                          #"FALCUN"
                          #]
        #sampling_names = list(sampling_strategies_ordered)
        learners_names = list(learners)

        sampling_names.append(" ")

        learners_ordered = ["knn_3", "svm_rbf", "mlp", "rf_entropy", "catboost", "xgb",
                            "tabnet", "tabpfn"]

        if learner == "knn_3":
            learner_name = "KNN"
        elif learner == "svm_rbf":
            learner_name = "SVM"
        elif learner == "mlp":
            learner_name = "MLP"
        elif learner == "rf_entropy":
            learner_name = "RF"
        elif learner == "catboost":
            learner_name = "Catboost"
        elif learner == "xgb":
            learner_name = "XGB"
        elif learner == "tabnet":
            learner_name = "Tabnet"
        elif learner == "tabpfn":
            learner_name = "TabPFN"


        learners_names.append(" ")
        ax.set_xticklabels(sampling_names, fontsize=40, rotation=45)
        ax.set_yticklabels(sampling_names, fontsize=40)
        ax.set_title("Setting: " + setting_name + ", Learner: " + learner_name,
                     fontsize=50)
        SAVE_PATH = "fig .pdf"


        if self.path_to_save is not None:
            PATH = self.path_to_save + "/" + str(filter_ids) +"/"
            if not os.path.exists(PATH):
                os.makedirs(PATH)
            SAVE_PATH = PATH + setting_name +  metric_name + "_"+str(learner) + ".pdf"
            print("SAVE PATH", SAVE_PATH)
            fig.savefig(SAVE_PATH, facecolor='white', transparent=True, bbox_inches='tight')
        #plt.show()
