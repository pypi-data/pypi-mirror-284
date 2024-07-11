import json
import os
import numpy as np
import pandas as pd
import pandas as pd
from py_experimenter.experimenter import PyExperimenter
from scipy.stats import ttest_ind_from_stats
from scipy.stats import ttest_ind as tt
from get_results import StudyData
from plot_functions import HeatMapPlot, BudgetPerformancePlot, WinMatrixPlot


# DEFINE METRIC, DATABASE NAME, GENERATE PANDAS DATAFRAME AND SAVE IT
def generate_aubc_df():
    grid = {}
    metric = ["test_accuracy"]

    db_name = "alpbench_ecai"
    setting_string = "small"
    db_config_file = "../../evaluation/experimenter/config/db_conf.yml"
    exp_scenario_file = "../../evaluation/experimenter/config/experiments.yml"
    grid["db_name"] = db_name
    grid["setting_name"] = setting_string
    source = db_config_file, exp_scenario_file

    studyData = StudyData(source=source, grid=grid)
    end_df = studyData.get_aubc_df()
    # check if path exists
    directory_path = "DATAFRAMES/" + setting_string + "/"
    if not os.path.exists(directory_path):
        print("does not exist")
        os.makedirs(directory_path)
    end_df.to_csv(directory_path + db_name +"_"+ setting_string + "_dynamic.csv")
    return end_df

# GENERATE BUDGET PERFORMANCE PLOT
def generate_budget_performance_plots():
    dataframe = pd.read_csv("DATAFRAMES/small/alpbench_ecai_small_dynamic.csv")

    openmlids = dataframe['openml_id'].unique()
    learners = dataframe['learner_name'].unique()

    collect_results = {}

    for learner in learners[:]:
        collect_results[learner] = {}
        for openmlid in openmlids[:]:
            perfPlot = BudgetPerformancePlot(dataframe, openmlid, learner, "test_accuracy")
            perfPlot.generate_plot_data()

            collect_results[learner][openmlid] = perfPlot.plot_data
            perfPlot.show()

    # save pkl file
    import pickle
    with open('saved_dictionary.pkl', 'wb') as f:
        pickle.dump(collect_results, f)

#generate_aubc_df()
generate_budget_performance_plots()


# GENERATE HEATMAPS

"""
dataframe = pd.read_csv("DATAFRAMES/small/alpbench_ecai_small_dynamic.csv")
learners = dataframe['learner_name'].unique()
filter = ["binary", "multi", "all"]
significance = [True, False]
for learner in learners[:1]:
    for f in filter[:1]:
        for s in significance[:]:
            heatMap = WinMatrixPlot(dataframe, learner, filter_ids=f, take_statistical_insignificant=s)
"""


# GENERATE WIN MATRICES