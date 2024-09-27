import os
import sys
import yaml
import dill
from recommender.exception import RecommenderException

def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise RecommenderException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj, file)
    
    except Exception as e:
        raise RecommenderException(e, sys)
    
def load_object(file_path: str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file {file_path} does not exist.")
        with open(file_path, "rb") as file:
            return dill.load(file)
        
    except Exception as e:
        raise RecommenderException(e, sys)