import os
import sys

import ast
import pandas as pd

from typing import List
from recommender.logger import logging
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from recommender.exception import RecommenderException
from recommender.entity.config_entity import DataTransformationConfig
from recommender.entity.artifact_entity import DataTransformationArtifact, DataIngestionArtifact
from recommender.utils.main_utils import save_object, read_yaml
from recommender.constant.training_pipeline import MERGE_COLUMN, SCHEMA_FILE_NAME, ITEM_NAME, COLUMN_NAME, JOB_NAME, CAST, CREW, OVERVIEW, GENRES, KEYWORDS, TAGS

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifact: DataIngestionArtifact):
        
        try:
            self.stemmer = PorterStemmer()
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_config = data_transformation_config
            self._schema_config = read_yaml(SCHEMA_FILE_NAME)
            
        except Exception as e:
            raise RecommenderException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)

        except Exception as e:
            raise RecommenderException(e, sys)

    @staticmethod    
    def convert(obj) -> List[str]:
        try:
            obj_list = ast.literal_eval(obj)
            return [item[ITEM_NAME] for item in obj_list]
        except (SyntaxError, ValueError, TypeError):
            return []

    @staticmethod    
    def convert3(obj) -> List[str]:
        genres = []
        counter = 0
        try:
            for i in ast.literal_eval(obj):
                if isinstance(i, dict) and ITEM_NAME in i:
                    genres.append(i[ITEM_NAME])
                    counter += 1
                    if counter == 3:
                        break
        except (SyntaxError, ValueError):
            pass
        return genres
    
    @staticmethod
    def fetch_director(obj):
        directors = []
        try:
            for i in ast.literal_eval(obj):
                if i[COLUMN_NAME]==JOB_NAME:
                    directors.append(i[ITEM_NAME])
            return directors
        except Exception as e:
            raise RecommenderException(e, sys)

    @staticmethod   
    def clean_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
        try:
            for column in columns:
                df[column] = df[column].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
            return df
        except Exception as e:
            raise RecommenderException(e, sys)

    def stem(self, text):
        try:
            y=[]
            for i in text.split():
                y.append(self.stemmer.stem(i))
            return " ".join(y)
        except Exception as e:
            raise RecommenderException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            
            movies_df = DataTransformation.read_data(self.data_ingestion_artifact.movies_file_path)

            credits_df = DataTransformation.read_data(self.data_ingestion_artifact.credits_file_path)

            movies_df= movies_df.merge(credits_df,on=MERGE_COLUMN)

            movies_df=movies_df[self._schema_config["columns"]]
            movies_df.dropna(inplace=True)

            columns_to_convert = self._schema_config["columns_to_convert"]
            for column in columns_to_convert:
                movies_df[column] = movies_df[column].apply(DataTransformation.convert)

            movies_df[CAST] = movies_df[CAST].apply(DataTransformation.convert3)

            movies_df[CREW] = movies_df[CREW].apply(DataTransformation.fetch_director)

            movies_df[OVERVIEW] = movies_df[OVERVIEW].apply(lambda x: x.split())

            columns_to_clean = self._schema_config["columns_to_clean"]
            movies_df = DataTransformation.clean_columns(movies_df, columns_to_clean)

            movies_df[TAGS] = movies_df[OVERVIEW] + movies_df[GENRES] + movies_df[CAST] + movies_df[CREW] + movies_df[KEYWORDS]

            movies = movies_df[self._schema_config["columns_to_use"]]

            movies.loc[:, TAGS] = movies[TAGS].apply(lambda x: ' '.join(x).lower())
            movies.loc[:, TAGS] = movies[TAGS].apply(self.stem)

            movies_file_path = self.data_transformation_config.transformed_movies_file_path
            
            movies_dir_path = os.path.dirname(movies_file_path)
            os.makedirs(movies_dir_path, exist_ok=True)
            movies.to_csv(movies_file_path, index=False, header=True)

            cv = CountVectorizer(max_features=5000, stop_words="english")
            vectors = cv.fit_transform(movies["tags"]).toarray()
            similarity = cosine_similarity(vectors)

            save_object(self.data_transformation_config.transformed_object_file_path, similarity)

            data_transformation_artifact = DataTransformationArtifact(transformed_object_file_path=self.data_transformation_config.transformed_object_file_path, transformed_movies_file_path=self.data_transformation_config.transformed_movies_file_path)

            logging.info(f"Data transformation artifact: {data_transformation_artifact}")

            return data_transformation_artifact
        
        except Exception as e:
            raise RecommenderException(e, sys)