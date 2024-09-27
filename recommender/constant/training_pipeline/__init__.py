import os

ITEM_NAME = "name"
MERGE_COLUMN = "title"
TITLE = "title"
TAGS = "tags"
CAST = "cast"
CREW = "crew"
GENRES = "genres"
OVERVIEW = "overview"
KEYWORDS = "keywords"
COLUMN_NAME = "job"
JOB_NAME = "Director"
MOVIES_PATH = os.path.join('artifact','data_transformation', 'transformed', 'movies.csv')
OBJECT_PATH = os.path.join('artifact','data_transformation', 'transformed_object', 'preprocessing.pkl')

PIPELINE_NAME = "recommender"
ARTIFACT_DIR = "artifact"
MOVIES_FILE_NAME = "movies.csv"
CREDITS_FILE_NAME = "credits.csv"
SCHEMA_FILE_NAME: str = os.path.join("config", "schema.yaml")


"""
data ingestion related constant values  
"""
DATA_INGESTION_MOVIES_COLLECTION_NAME: str = "movies"
DATA_INGESTION_CREDITS_COLLECTION_NAME: str = "credits"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

"""
data transformation related constant values
"""
PREPROCESSING_FILE_NAME = "preprocessing.pkl"
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"
