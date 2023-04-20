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
Model Trainer related constants
'''
MODEL_TRAINER_DIR_NAME : str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME : str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int =  1
MODEL_TRAINER_BATCH_SIZE: int = 16


'''
Model Pusher related constants
'''
BUCKET_NAME = "sign-lang-1811"
S3_MODEL_NAME = "best.pt"