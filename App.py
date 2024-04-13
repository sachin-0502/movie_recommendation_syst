import streamlit as st
import pickle
import pandas as pd




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # return index of given movie
    distances = similarity[movie_index]  # fetch similarity score array of that particular movie

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # reverse true for descending order sorting

    recommended_movies = []
    for i in movie_list:

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("MOVIE RECOMMENDATION SYSTEM\n")               # streamlit heading textbox 

selected_movie_name = st.selectbox(                      # streamlit selectbox code
    "Select Movie Name",
    movies['title'].values
)

if st.button("Recommend Best Matches\n"):                         # streamlit button code 
    recommendations = recommend(selected_movie_name)
    number = 1
    for i in recommendations:
        st.write(f"{number}. {i}")
        number +=1
