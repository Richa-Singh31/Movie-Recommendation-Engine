from recommender.exception import RecommenderException
from recommender.logger import logging
import os
import sys
from recommender.entity.config_entity import DataIngestionConfig
from recommender.entity.artifact_entity import DataIngestionArtifact
from recommender.data_access.recommender_data import RecommenderData

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise RecommenderException(e, sys)
        
    def export_data_into_feature_store(self) -> None:
        """
        Export mongo db collection record as dataframe into feature
        """
        try:
            logging.info("Exporting data from mongodb to feature store")
            
            recommender_data = RecommenderData()
            
            movies_dataframe = recommender_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.movies_collection_name)
            credits_dataframe = recommender_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.credits_collection_name)

            movies_file_path = self.data_ingestion_config.movies_file_path
            credits_file_path = self.data_ingestion_config.credits_file_path

            movies_dir_path = os.path.dirname(movies_file_path)
            os.makedirs(movies_dir_path, exist_ok=True)
            movies_dataframe.to_csv(movies_file_path, index=False, header=True)

            credits_dir_path = os.path.dirname(credits_file_path)
            os.makedirs(credits_dir_path, exist_ok=True)
            credits_dataframe.to_csv(credits_file_path, index=False, header=True)

        except Exception as e:
            raise RecommenderException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.export_data_into_feature_store()

            data_ingestion_artifact = DataIngestionArtifact(movies_file_path=self.data_ingestion_config.movies_file_path, credits_file_path=self.data_ingestion_config.credits_file_path)

            return data_ingestion_artifact
        
        except Exception as e:
            raise RecommenderException(e, sys)
    