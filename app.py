import ast
import pandas as pd
import streamlit as st
import requests
import os

# Google Drive direct download URLs
MOVIES_URL = "https://drive.google.com/uc?export=download&id=1V9dVf03-4B92vRv6TyI-LAFF4sNiEVRu"
CREDITS_URL = "https://drive.google.com/uc?export=download&id=16T6VczZmXpjHqWhmJORHcHXiEJxPHaQO"

# Function to download a file from Google Drive
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

# Define file paths
movies_path = "movies.csv"
credits_path = "credits.csv"

# Download the files if not exist
if not os.path.exists(movies_path):
    print("Downloading movies.csv...")
    download_file(MOVIES_URL, movies_path)

if not os.path.exists(credits_path):
    print("Downloading credits.csv...")
    download_file(CREDITS_URL, credits_path)

# Load the datasets
movies = pd.read_csv(movies_path)
credits = pd.read_csv(credits_path)

# Merge movies and credits
movies = movies.merge(credits, on='title')

# Keep necessary columns
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

# Function to extract names from a list of dictionaries
def extract_names(obj):
    L = []
    for item in ast.literal_eval(obj):
        L.append(item['name'])
    return L

# Function to extract top 3 cast members
def extract_top_cast(obj):
    L = []
    counter = 0
    for item in ast.literal_eval(obj):
        if counter != 3:
            L.append(item['name'])
            counter += 1
        else:
            break
    return L

# Function to extract director's name
def extract_director(obj):
    L = []
    for item in ast.literal_eval(obj):
        if item['job'] == 'Director':
            L.append(item['name'])
            break
    return L

# Fill missing values
movies.dropna(inplace=True)

# Process columns
movies['genres'] = movies['genres'].apply(extract_names)
movies['keywords'] = movies['keywords'].apply(extract_names)
movies['cast'] = movies['cast'].apply(extract_top_cast)
movies['crew'] = movies['crew'].apply(extract_director)

# Convert overview into list of words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces in multi-word names
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create a new "tags" column
movies['tag'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
movies['tag'] = movies['tag'].apply(lambda x: " ".join(x))

# Final dataset
final_movies = movies[['movie_id', 'title', 'tag']]

# Text vectorization
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(final_movies['tag']).toarray()

# Calculate cosine similarity
sim_mat = cosine_similarity(vectors)

# TMDb API key
api_key = "8265bd1679663a7ea12ac168da84d2e8"

# Streamlit app starts here
st.title('🎬 Movie Recommender System')

# Dropdown to select a movie
selected_movie = st.selectbox(
    "Please select a movie to get suggestions",
    final_movies['title'].values
)

# Function to fetch poster from TMDb API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/original{poster_path}"
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Image"

# Function to recommend movies
def recommend(movie):
    index_mov = final_movies[final_movies['title'] == movie].index[0]
    distances = sim_mat[index_mov]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = final_movies.iloc[i[0]].movie_id
        recommended_movies.append(final_movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# Font style for movie names
font_style = "font-family: Arial, sans-serif; font-size: 24px;"

# Recommend button
if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(len(names))
    for i in range(len(names)):
        with cols[i]:
            st.markdown(f"<span style='{font_style}'>{names[i]}</span>", unsafe_allow_html=True)
            st.image(posters[i], use_container_width=True)
