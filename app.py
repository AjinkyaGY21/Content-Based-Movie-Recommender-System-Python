import pickle
import streamlit as st
import requests
import pandas as pd

movie_dict = pickle.load(open(r"E:\NEW_FOLDER\Projects_Java_Python\Movie Recommender System\movie_dict.pkl", "rb"))

movies = pd.DataFrame(movie_dict)

sim_mat = pickle.load(open(r"E:\NEW_FOLDER\Projects_Java_Python\Movie Recommender System\sim_mat.pkl", "rb"))

api_key = "8265bd1679663a7ea12ac168da84d2e8"
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Please, enter a movie to get suggestions ",
    movies["title"].values)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data)
    poster_path = data.get("poster_path")
    return f"https://image.tmdb.org/t/p/original{poster_path}"

def recommend(movie):
    index_mov = movies[movies["title"]==movie].index[0]
    dist_mov = sim_mat[index_mov]
    sim_mov_rec = sorted(list(enumerate(dist_mov)), reverse = True, key = lambda x:x[1])[1:6]
    
    rec_movies = []
    rec_movies_posters = []
    
    for i in sim_mov_rec:
        mov_id = movies.iloc[i[0]].movie_id
        
        #fetch poster from API
        rec_movies.append(movies.iloc[i[0]].title)  
        rec_movies_posters.append(fetch_poster(mov_id))   
                           
    return rec_movies, rec_movies_posters           
  
font_style = "font-family: Arial, sans-serif; font-size: 24px;"

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    cols = st.columns(len(names))
    # Iterate over the recommended movies and posters
    for i in range(len(names)):
        # Display the movie name in a single horizontal line
        cols[i].write(f"<span style='{font_style}'>{names[i]}</span>", unsafe_allow_html=True)

        # Display the movie poster below the corresponding name
        cols[i].image(posters[i], use_column_width=True)
