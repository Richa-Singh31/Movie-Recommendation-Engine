import sys
from recommender.exception import RecommenderException
from recommender.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        raise RecommenderException(e, sys)
