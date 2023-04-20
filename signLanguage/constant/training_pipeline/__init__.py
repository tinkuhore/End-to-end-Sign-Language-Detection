import os

ARTIFACTS_DIR : str = "artifacts"

'''
data ingestion related constants
'''
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "features_store"
DATA_DOWNLOAD_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"


'''
data validation related constants
'''
DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_STATUS_FILE : str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


'''
training related constants
'''