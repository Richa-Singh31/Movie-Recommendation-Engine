import sys
from recommender.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataTransformationConfig
from recommender.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact
from recommender.exception import RecommenderException
from recommender.logger import logging
from recommender.components.data_ingestion import DataIngestion
from recommender.components.data_transformation import DataTransformation

class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logging.info("Starting data ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise RecommenderException(e, sys) 
    
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            self.data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_transformation_config=self.data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info(f"Data transformation completed and artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise RecommenderException(e, sys)           

    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()

            data_transformation_artifact: DataTransformationArtifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)

        except Exception as e:
            raise RecommenderException(e, sys)