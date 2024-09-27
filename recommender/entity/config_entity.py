import os
from datetime import datetime
from recommender.constant import training_pipeline
        
class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now()):
        self.timestamp = timestamp.strftime("%m-%d-%Y_%H-%M-%S")
        self.pipeline_name = os.path.join(training_pipeline.PIPELINE_NAME, self.timestamp) 
        self.artifact_dir = training_pipeline.ARTIFACT_DIR
        self.timestamp:str = self.timestamp

class DataIngestionConfig:

    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> None:
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        
        self.movies_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.MOVIES_FILE_NAME)
        self.credits_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.CREDITS_FILE_NAME)

        self.movies_collection_name: str = training_pipeline.DATA_INGESTION_MOVIES_COLLECTION_NAME
        self.credits_collection_name: str = training_pipeline.DATA_INGESTION_CREDITS_COLLECTION_NAME

class DataTransformationConfig:
    
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)

        self.transformed_movies_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, training_pipeline.MOVIES_FILE_NAME)

        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, training_pipeline.PREPROCESSING_FILE_NAME)
