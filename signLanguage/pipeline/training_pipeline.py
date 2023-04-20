import sys, os
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation

from signLanguage.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig)

from signLanguage.entity.artifact_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()


    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
        


    def start_data_validation(self,
                              data_ingestion_artifact: DataIngestionArtifact
                              )->DataIngestionArtifact:
        logging.info("Entered Data Validation method of Training Pipeline class")

        try:
            data_validation = DataValidation(
                data_validation_config =  self.data_validation_config,
                data_ingestion_artifact = data_ingestion_artifact
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Exited Data Validation method of Training Pipeline class")

            return data_validation_artifact

        except Exception as e:
            raise SignException(e, sys)

    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact)
            
            if data_validation_artifact.validation_status :
                pass
        
        except Exception as e:
            raise SignException(e, sys)