# Movie Recommendation System

## Description
This is a movie recommendation engine which takes in a movie name and recommends ten most similar movies based on various parameters such as the genres, cast, crew, overview and director of the movie.

## Dataset
The dataset used is publicly available and can be downloaded through the provided link:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


## Key Components
- Data Ingestion: The DataIngestion class exports data from MongoDB collections into CSV files for a movie recommender system, managing directory creation and file saving based on configurations, and returns a DataIngestionArtifact with the file paths.
- Data Transformation: The DataTransformation class processes and transforms movie data from CSV files, merging movie and credits data, cleaning and converting relevant fields, and generating tags for each movie. It utilizes NLP techniques for stemming and vectorization, ultimately saving the transformed data and a similarity matrix for use in a movie recommender system.
- Training Pipeline: 
The TrainPipeline class manages the training process by orchestrating data ingestion and transformation. It initializes configurations, executes the data ingestion process, and transforms the data, while logging the progress and handling any exceptions that arise.
- Recommender: The movie recommender component using Streamlit, allows users to select a movie and receive a list of similar movie recommendations based on a precomputed similarity matrix.

## Install Dependencies
```bash
pip install -r requirements.txt
```
## Train the model
```bash
python main.py
```
## Run the app
```bash
streamlit run app.py
```
## Conclusion
This project implements a movie recommendation system that encompasses data ingestion and transformation processes. It integrates various components such as data extraction from MongoDB, preprocessing of movie data, and recommendation algorithms using machine learning techniques. The pipeline ensures a streamlined workflow, enabling efficient handling of datasets, facilitating user interaction through a web interface, and ultimately delivering personalized movie recommendations based on user preferences.
