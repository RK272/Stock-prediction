from src.entity.artifact_entity import regressionMetricArtifact
from src.exception import SensorException
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import os,sys
import numpy as np

def get_regression_score(y_true,y_pred)->regressionMetricArtifact:
    try:
        model_mse = mean_squared_error(y_true, y_pred)
        model_rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        model_mae=mean_absolute_error(y_true,y_pred)
        model_r2=r2_score(y_true,y_pred)

        regression_metric =  regressionMetricArtifact(mse=model_mse,
                    rmse=model_rmse,
                    mae=model_mae,
                    r2=model_r2)
        return regression_metric
    except Exception as e:
        raise SensorException(e,sys)