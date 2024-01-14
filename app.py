import streamlit as st
import pickle
import requests

API_KEY = "b49f3c64bcdd960239e4da7308df08fd"
BASE_PATH = "https://image.tmdb.org/t/p/w500"

def get_poster_id(ID):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=".format(ID)+API_KEY)
    data = response.json()
    return data['poster_path']

st.title('Movie recommended system')

final_df = pickle.load(open('model/data.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

def get_recommedation(movie):
    movie_list = []
    id = final_df[final_df['title'] == movie].index[0]
    movie_list_id = sorted(list(enumerate(similarity[id])),reverse=True,key=lambda x:x[1])
    for i in movie_list_id[1:6]:
        movie_list.append(final_df.loc[i[0]])
    return movie_list

option = st.selectbox(
    'Enter your favroite movie name',
    final_df.title
    )

if st.button("recommended"):
    recommedation =  get_recommedation(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(BASE_PATH+get_poster_id(recommedation[0]['movie_id']))
        col1.write(recommedation[0]['title'])
    with col2:  
        st.image(BASE_PATH+get_poster_id(recommedation[1]['movie_id']))
        col2.write(recommedation[1]['title'])
    with col3:
        st.image(BASE_PATH+get_poster_id(recommedation[2]['movie_id']))
        col3.write(recommedation[2]['title'])
    with col4:
        st.image(BASE_PATH+get_poster_id(recommedation[3]['movie_id']))
        col4.write(recommedation[3]['title'])
    with col5:
        st.image(BASE_PATH+get_poster_id(recommedation[4]['movie_id']))
        col5.write(recommedation[4]['title'])
