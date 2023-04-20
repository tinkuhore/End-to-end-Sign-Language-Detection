from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.logger import logging

obj = TrainPipeline()
obj.run_pipeline()
print("Model Pushed successfully")
logging.info("Job Done!")