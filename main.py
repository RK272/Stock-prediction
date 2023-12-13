from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import SensorException
import os,sys
from src.logger import logging
from src.pipeline import training_pipeline
from src.pipeline.training_pipeline import TrainPipeline
import os
from src.utils.main_utils import read_yaml_file
from src.constant.training_pipeline import SAVED_MODEL_DIR


if __name__ =='__main__':
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

    except Exception as e:
        print(e)
        logging.exception(e)




