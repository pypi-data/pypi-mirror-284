import numpy as np
from py_experimenter.exceptions import DatabaseConnectionError
from py_experimenter.experimenter import PyExperimenter, ResultProcessor
import types

from alpbench.benchmark.BenchmarkConnector import MySQLBenchmarkConnector, DataFileBenchmarkConnector
from alpbench.benchmark.BenchmarkSuite import (
    OpenMLBenchmarkSuite,
    TabZillaBenchmarkSuite
)
from alpbench.evaluation.experimenter.LogTableObserver import LogTableObserver, SparseLogTableObserver
from alpbench.pipeline.ActiveLearningPipeline import ActiveLearningPipeline
from alpbench.pipeline.Oracle import Oracle

import xgboost as xgb
import catboost as cb

from sklearn.ensemble import (
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from tabpfn import TabPFNClassifier
from alpbench.util.pytorch_tabnet.tab_model import TabNetClassifier
from alpbench.benchmark.BenchmarkConnector import MySQLBenchmarkConnector, DataFileBenchmarkConnector

from alpbench.pipeline.QueryStrategy import (
    BALDQueryStrategy,
    ClusterMarginQueryStrategy,
    CoreSetQueryStrategy,
    DiscriminativeQueryStrategy,
    EntropyQueryStrategy,
    EpistemicUncertaintyQueryStrategy,
    FalcunQueryStrategy,
    KMeansQueryStrategy,
    LeastConfidentQueryStrategy,
    MarginQueryStrategy,
    MaxEntropyQueryStrategy,
    MinMarginQueryStrategy,
    MonteCarloEERLogLoss,
    MonteCarloEERMisclassification,
    PowerBALDQueryStrategy,
    PowerMarginQueryStrategy,
    QBCVarianceRatioQueryStrategy,
    QueryByCommitteeEntropyQueryStrategy,
    QueryByCommitteeKLQueryStrategy,
    RandomMarginQueryStrategy,
    RandomQueryStrategy,
    TypicalClusterQueryStrategy,
    WeightedClusterQueryStrategy
)
from alpbench.benchmark.ActiveLearningScenario import ActiveLearningScenario
from alpbench.benchmark.ActiveLearningSetting import ActiveLearningSetting

#exp_learner_sampler_file = "config/exp_learner_sampler.yml"
exp_learner_sampler_file = "config/experiments.yml"
db_config_file = "config/db_conf.yml"

default_learners = {
    "svm_lin": SVC(kernel='linear', probability=True),
    "svm_rbf": SVC(kernel='rbf', probability=True),
    "rf_entropy": RandomForestClassifier(n_estimators=100, max_depth=10, criterion='entropy'),
    "rf_gini": RandomForestClassifier(n_estimators=100, max_depth=10, criterion='gini'),
    "rf_entropy_large": RandomForestClassifier(n_estimators=250, max_depth=10, criterion='entropy'),
    "rf_gini_large": RandomForestClassifier(n_estimators=250, max_depth=10, criterion='gini'),
    "knn_3": KNeighborsClassifier(n_neighbors=3),
    "knn_10": KNeighborsClassifier(n_neighbors=10),
    "log_reg": LogisticRegression(),
    "multinomial_bayes": MultinomialNB(),
    "etc_entropy": ExtraTreesClassifier(n_estimators=100, max_depth=10, criterion='entropy'),
    "etc_gini": ExtraTreesClassifier(n_estimators=100, max_depth=10, criterion='gini'),
    "etc_entropy_large": ExtraTreesClassifier(n_estimators=250, max_depth=10, criterion='entropy'),
    "etc_gini_large": ExtraTreesClassifier(n_estimators=250, max_depth=10, criterion='gini'),
    "naive_bayes": GaussianNB(),
    "mlp": MLPClassifier(),
    "GBT_logloss": GradientBoostingClassifier(n_estimators=100),
    "GBT_exp": GradientBoostingClassifier(n_estimators=100, loss='exponential'),
    "GBT_logloss_large": GradientBoostingClassifier(n_estimators=250),
    "tabpfn": TabPFNClassifier(device='cpu', N_ensemble_configurations=32),
    "xgb": xgb.XGBClassifier(tree_method='hist', max_depth=6, n_estimators=100),
    "catboost": cb.CatBoostClassifier(rsm=0.1, iterations=100, depth=10, verbose=0, boosting_type='Plain', bootstrap_type='Bernoulli', subsample=.75),
    "tabnet": TabNetClassifier(verbose=0)
}

default_query_strategies = {
    "random": RandomQueryStrategy(42),
    "random_margin": RandomMarginQueryStrategy(42),
    "cluster_margin": ClusterMarginQueryStrategy(42),
    "core_set": CoreSetQueryStrategy(42),
    "epistemic": EpistemicUncertaintyQueryStrategy(42),
    "entropy": EntropyQueryStrategy(42),
    "falcun": FalcunQueryStrategy(42),
    "margin": MarginQueryStrategy(42),
    "max_entropy": MaxEntropyQueryStrategy(42, 10),
    "least_confident": LeastConfidentQueryStrategy(42),
    "mc_logloss": MonteCarloEERLogLoss(42),
    "mc_misclass": MonteCarloEERMisclassification(42),
    "kmeans": KMeansQueryStrategy(42),
    "discrim": DiscriminativeQueryStrategy(42),
    "qbc_entropy": QueryByCommitteeEntropyQueryStrategy(42, 10),
    "qbc_kl": QueryByCommitteeKLQueryStrategy(42, 10),
    "bald": BALDQueryStrategy(42, 10),
    "power_margin": PowerMarginQueryStrategy(42),
    "min_margin": MinMarginQueryStrategy(42, 10),
    "typ_cluster": TypicalClusterQueryStrategy(42),
    "weighted_cluster": WeightedClusterQueryStrategy(42),
    "qbc_variance_ratio": QBCVarianceRatioQueryStrategy(42, 10),
    "power_bald": PowerBALDQueryStrategy(42, 10),
}


tabzilla = TabZillaBenchmarkSuite()
tabzilla_ids = tabzilla.get_openml_dataset_ids()
cc18 = OpenMLBenchmarkSuite(99)
cc18_ids = cc18.get_openml_dataset_ids()


class ExperimentRunner:

    def __init__(self, db_credentials, db_name):
        self.db_credentials = db_credentials
        self.db_name = db_name

    def run_experiment(self, parameters: dict, result_processor: ResultProcessor, custom_config: dict):

        dbbc = MySQLBenchmarkConnector(host=self.db_credentials["host"], user=self.db_credentials["user"],
                                       password=self.db_credentials["password"], database=self.db_name, use_ssl=False)
        #try:
        connector: MySQLBenchmarkConnector = dbbc

        OPENML_ID = int(parameters["openml_id"])
        SETTING_NAME = parameters["setting_name"]
        TEST_SPLIT_SEED = int(parameters["test_split_seed"])
        TRAIN_SPLIT_SEED = int(parameters["train_split_seed"])
        SEED = int(parameters["seed"])

        setting = ActiveLearningSetting(setting_id=4, setting_name='small_dynamic', setting_test_size=0.33,
                              setting_train_type='absolute', setting_labeled_train_size=30,
                              number_of_iterations=1, number_of_queries=1, factor=5)


        scenario = connector.load_or_create_scenario(openml_id=OPENML_ID, test_split_seed=TEST_SPLIT_SEED,
                                                     train_split_seed=TRAIN_SPLIT_SEED, seed=SEED,
                                                     setting_id=setting.get_setting_id())

        X_l, y_l, X_u, y_u, X_test, y_test = scenario.get_data_split()

        query_strat_name = parameters["query_strategy_name"]
        learner_name = parameters["learner_name"]


        if learner_name == "tabpfn":
            if X_l.shape[-1]>100 or len(np.unique(y_l))>10:
                dbbc.close()
                return

        LEARNER = default_learners[learner_name]

        task_dependent_query_budget = setting.factor * len(np.unique(np.concatenate(([y_l,y_u,y_test]))))
        setting.number_of_queries = task_dependent_query_budget

        QUERY_STRATEGY = default_query_strategies[query_strat_name]
        LEARNER = default_learners[learner_name]

        #OBSERVER = [LogTableObserver(result_processor, X_test, y_test)]
        OBSERVER = [SparseLogTableObserver(result_processor, X_test, y_test)]


        ALP = ActiveLearningPipeline(learner=LEARNER, query_strategy=QUERY_STRATEGY, observer_list=OBSERVER,
                                     num_iterations=setting.get_number_of_iterations(),
                                     num_queries_per_iteration=setting.get_number_of_queries())

        oracle = Oracle(X_u, y_u)
        ALP.active_fit(X_l, y_l, X_u, oracle)
        #finally:
        print("closing connection")
        dbbc.close()


def run_parallel(variable, default_setup=False, run_setup=False, reset_experiments=False):

    experimenter = PyExperimenter(experiment_configuration_file_path=exp_learner_sampler_file,
                                  database_credential_file_path=db_config_file,
                                  name=variable)

    db_name = experimenter.config.database_configuration.database_name
    db_credentials = experimenter.db_connector._get_database_credentials()

    if run_setup:
        #from DefaultSetup import ensure_default_setup
        #dbbc = MySQLBenchmarkConnector(host=db_credentials["host"], user=db_credentials["user"],
        #                               password=db_credentials["password"], database=db_name, use_ssl=False)
        #ensure_default_setup(dbbc=dbbc)

        setting_combinations = []

        filter_out = [1567,1169,41147,1493]
        setting_combinations += [{'setting_name': 'small', 'openml_id': oid, 'train_split_seed': seed} for oid in cc18_ids if oid not in filter_out for seed in np.arange(20)]


        if reset_experiments:
            experimenter.reset_experiments('running')#, 'failed', 'error')
        else:
            experimenter.fill_table_from_combination(
                parameters={

                    "learner_name": ["rf_entropy",
                                    "tabpfn",
                                     "catboost"
                                     ],
                    "query_strategy_name": ["margin",
                                            "entropy",
                                            "cluster_margin", "typ_cluster",
                                            "random"
                    ],
                    "test_split_seed": np.arange(1),
                    #"train_split_seed": np.arange(1),
                    "seed": np.arange(1)
                },
                fixed_parameter_combinations=setting_combinations)

    else:
        er = ExperimentRunner(db_credentials, db_name)
        experimenter.execute(er.run_experiment, -1)

def main():
    import sys


    variable_job_id = str(sys.argv[1])
    variable_task_id = str(sys.argv[2])


    # concatenate both variables with _
    variable = variable_job_id + "_" + variable_task_id

    run_parallel(variable, run_setup = True, reset_experiments = True)
    #run_parallel(variable)



if __name__ == "__main__":
    main()
