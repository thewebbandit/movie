import streamlit as st

st.title('recommend movie based on content')

import pickle
movie_df = pickle.load(open('movies.pkl', 'rb'))
movie_list = movie_df['title'].values
similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox('select movie on which recommendations required',movie_list)

def recommend(movie):
    recommended_movies = []
    movie_index = movie_df[movie_df['title'] == movie].index[0]
    distances = similarity_matrix[movie_index]
    movie_list_ = sorted(enumerate(distances), key = lambda x :x[1], reverse = True)[1:6]
    
    
    for i in movie_list_:
        ind = i[0]
        recommended_movies.append(movie_df['title'][ind])
        movie_id = i[0]
    return recommended_movies

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
