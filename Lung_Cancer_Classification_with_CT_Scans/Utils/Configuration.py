def loadConfig() -> dict:
    """
    # Description
        -> This function aims to store all the configuration related parameters used inside the project.
    ----------------------------------------------------------------------------------------------------
    := return: Dictionary with some of the important file paths of the project.
    """
    return {
        'pylidcFeaturesFilename':'./Datasets/pylidc_features.csv',
        'multiClassPylidcFeaturesFilename':'./Datasets/multi_class_pylidc_features.csv',
        'binaryPylidcFeaturesFilename':'./Datasets/binary_pylidc_features.csv',
        'pyradiomicsFeaturesFilename':'./Datasets/pyradiomics_features.csv',
        'pyradiomicsRefactoredFeaturesFilename':'./Datasets/refactored_pyradiomics_features.csv',
        'finalFeaturesDatasetFilename':'./Datasets/final_features_dataset.csv',
        'metricsDatasetFilename':'./Datasets/metrics_collected.csv',
    }

def loadModelsPaths() -> dict:
    """
    # Description
        -> Loads a dictionary with important paths when analysing a model's performance.
    ------------------------------------------------------------------------------------
    := return: Dictionary with all the paths used to stored model related data.
    """
    return {
        'SVC':{
            'accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/accuracy/evaluationPlot.png'
            },
            'balanced_accuracy':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/balanced_accuracy/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/balanced_accuracy/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/balanced_accuracy/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/balanced_accuracy/evaluationPlot.png'
            },
            'recall':{
                # Obtained through Grid Search
                'bestParamsPath':'./ExperimentalResults/SVM/recall/bestParams.json',
                'bestEstimatorPath':'./ExperimentalResults/SVM/recall/bestEstimator.pkl',

                # Obtained through Group K-Fold Cross Validation
                'modelEvaluationMetrics':'./ExperimentalResults/SVM/recall/evaluationMetrics.json',
                'modelEvaluationPlot':'./ExperimentalResults/SVM/recall/evaluationPlot.png'
            }
        

        

                }
    }

def loadModelsParameterGrids() -> dict:
    """
    # Description
        -> This function focuses on storing the possible paramaters configurations of
        some machine learning algorithms to be used alongside GridSearch.
    ---------------------------------------------------------------------------------
    := return: Dictionary with all the parameter grids used on each model Grid Search.
    """
    return {
        

        'SVC':{
            'C': [0.1, 1, 10, 100],
            'kernel': ['linear', 'rbf', 'poly'],
            'gamma': ['scale', 'auto'],
            'degree': [2, 3, 4],
            'coef0': [0.0, 0.1, 0.5],
            'probability': [True]
        }
    }