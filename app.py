import os
import sys
import streamlit as st
import pandas as pd
from recommender.utils.main_utils import load_object
from recommender.constant.training_pipeline import MOVIES_PATH, OBJECT_PATH, TITLE
from recommender.exception import RecommenderException

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
MOVIES_FILE_PATH = os.path.join(BASE_DIR, MOVIES_PATH)
SIMILARITY_FILE_PATH = os.path.join(BASE_DIR, OBJECT_PATH)

movies = pd.read_csv(MOVIES_FILE_PATH)
similarity = load_object(file_path=SIMILARITY_FILE_PATH)

def recommend(movie):
    try:
        movie_index = movies[movies[TITLE]==movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:11]
        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]][TITLE])
        return recommended_movies
        
    except Exception as e:
        raise RecommenderException(e, sys)


st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie", movies[TITLE].values)

if st.button("Recommend"):
    recommended_movies = recommend(selected_movie_name)
    for i in recommended_movies:
        st.write(i)
