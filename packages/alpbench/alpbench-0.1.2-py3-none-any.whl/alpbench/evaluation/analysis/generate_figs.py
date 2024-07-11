import json
import os
import numpy as np
import pandas as pd
import pandas as pd
from py_experimenter.experimenter import PyExperimenter
from scipy.stats import ttest_ind_from_stats
from scipy.stats import ttest_ind as tt
from get_results import StudyData



# DEFINE METRIC, DATABASENAME, GENERATE PANDAS DATAFRAME AND SAVE IT
grid = {}
metric = ["test_accuracy"]

db_name = "alpbench_ecai"
setting_string = "small"
db_config_file = "../../evaluation/experimenter/config/db_conf.yml"
exp_scenario_file = "../../evaluation/experimenter/config/experiments.yml"
grid["db_name"] = db_name
grid["setting_name"] = setting_string


source = db_config_file, exp_scenario_file
studyData = StudyData(source=source, grid=grid, csv_path=f"results/dataframes/")
end_df = studyData.get_aubc_df()
# check if path exists
directory_path = "DATAFRAMES/" + setting_string + "/"
if not os.path.exists(directory_path):
    print("does not exist")
    os.makedirs(directory_path)
end_df.to_csv(directory_path + db_name +"_"+ setting_string + "_dynamic.csv")



#learners = ["rf_entropy", "tabpfn", "catboost"]
#query_strategies = ["margin", "entropy", "cluster_margin", "typ_cluster", "random"]