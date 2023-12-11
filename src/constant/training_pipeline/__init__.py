import os

PIPELINE_NAME:str ="stock"
ARTIFACT_DIR:str ="artifact"
DATA_INGESTION_DIR_NAME:str ="data_ingestion"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "stock"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

SAVED_MODEL_DIR =os.path.join("saved_models")
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
FILE_NAME: str = "stock.csv"