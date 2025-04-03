import pickle
import streamlit as st
import requests
import pandas as pd
import os


# Google Drive direct download URLs
MOVIE_DICT_URL = "https://drive.google.com/uc?export=download&id=1agHhtrmIQ4i4B-dhyuH8ryAWtZAon-SW"
SIM_MAT_URL = "https://drive.google.com/uc?export=download&id=1EbEPHAn-2ONVw5_nqEbglQxEYi5GZgs7"


# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


# Define file paths
movie_dict_path = "movie_dict.pkl"
sim_mat_path = "sim_mat.pkl"


# Download the files if they do not exist
if not os.path.exists(movie_dict_path):
    print("Downloading movie_dict.pkl...")
    download_file(MOVIE_DICT_URL, movie_dict_path)

if not os.path.exists(sim_mat_path):
    print("Downloading sim_mat.pkl...")
    download_file(SIM_MAT_URL, sim_mat_path)

# Load the pickle files
with open(movie_dict_path, "rb") as f:
    movie_dict = pickle.load(f)

with open(sim_mat_path, "rb") as f:
    sim_mat = pickle.load(f)


print("Files loaded successfully!")


movies = pd.DataFrame(movie_dict)


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
