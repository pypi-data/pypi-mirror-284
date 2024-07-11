import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
import pandas as pd
from py_experimenter.experimenter import PyExperimenter
import json
import os
from scipy.stats import ttest_ind_from_stats
from scipy.stats import ttest_ind as tt


class StudyData():

    def __init__(self):

    def get_aubc_df(self):
        pass

class StudyDataFromFile(StudyData):




class StudyDataFromDatabase(StudyData):
    def __init__(self, source, grid):
        self.db_config, self.scenario_config = source
        self.grid = grid
        self.setting = self.grid["setting_name"]

    def get_aubc_df(self):

        db_name = self.grid["db_name"]
        experimenter_scenarios = PyExperimenter(experiment_configuration_file_path=self.scenario_config,
                                                database_credential_file_path=self.db_config)
        results = experimenter_scenarios.get_table()
        results = results.rename(columns={'ID': 'experiment_id'})
        accuracies = experimenter_scenarios.get_logtable('accuracy_log')
        experiment_ids = results['experiment_id'].values
        print(results['learner_name'].unique())
        print(results['query_strategy_name'].unique())

        labeling = experimenter_scenarios.get_logtable('labeling_log')



        files_exist = False
        if os.path.exists("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+ self.setting +  "_accuracies.csv"):
            files_exist = True
            print("FILE EXISTS")
            loaded_accuracies = pd.read_csv("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+ self.setting + "_accuracies.csv")
            loaded_labeling = pd.read_csv("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+ self.setting + "_labeling.csv")
            loaded_results = pd.read_csv("DATAFRAMES/"+ self.setting + "/"+ db_name +"_"+self.setting + "_results.csv")
            pre_df = pd.read_csv("DATAFRAMES/" + self.setting + "/" + db_name +"_"+ self.setting + "_dynamic.csv")


        if not os.path.exists("DATAFRAMES/" + self.setting + "/"):
            os.makedirs("DATAFRAMES/" + self.setting + "/")

        results.to_csv("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+ self.setting +  "_results.csv")
        accuracies.to_csv("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+self.setting +  "_accuracies.csv")
        labeling.to_csv("DATAFRAMES/"+ self.setting + "/" + db_name +"_"+self.setting +  "_labeling.csv")


        data = accuracies['model_dict'].values
        max_iter = 20

        exp_ids = []
        for i in experiment_ids[:]:
            if i in labeling['experiment_id'].values and i in accuracies['experiment_id'].values:
                if files_exist:
                    if i not in loaded_labeling['experiment_id'].values and i not in loaded_accuracies['experiment_id'].values:
                        exp_ids.append(i)
                else:
                    exp_ids.append(i)

        dict_to_fill = pd.DataFrame(columns=['experiment_id', 'iteration', 'test_accuracy', 'test_f1',
                                                'test_precision', 'test_recall', 'test_auc', 'test_log_loss',
                                                'len_X_l'])

        for enum,i in enumerate(exp_ids[:]):
            if enum%100 == 0:
                print("Experiment", enum, "of", len(exp_ids))
            for j in range(int(max_iter) + 1):
                lab = labeling[labeling['experiment_id'] == i]
                label = lab['data_dict'].values
                actual_max_iter = max(map(int, json.loads(data[0]).keys()))
                if j > actual_max_iter:
                    continue
                label_dict = json.loads(label[0])[str(j)]
                acc = accuracies[accuracies['experiment_id'] == i]
                data = acc['model_dict'].values
                dict = json.loads(data[0])[str(j)]
                dict_to_fill.loc[len(dict_to_fill)] = [int(i), int(dict['iteration']), dict['test_accuracy'],
                                                        dict['test_f1'],
                                                        dict['test_precision'], dict['test_recall'],
                                                        dict['test_auc'], dict['test_log_loss'],
                                                        int(label_dict['len_X_l'])]

        merged_df = pd.merge(results, dict_to_fill, on='experiment_id', how='inner')
        merged_df = merged_df[['setting_name', 'openml_id', 'learner_name', 'query_strategy_name',
                                'test_split_seed', 'train_split_seed', 'seed', 'iteration', 'test_accuracy',
                                'test_f1',
                                'test_precision', 'test_recall', 'test_auc', 'test_log_loss', 'len_X_l']]
        end_df = merged_df

        if files_exist:
            end_df = pd.concat([pre_df, end_df], axis=0)
        return end_df
(