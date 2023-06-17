# Movie Recommender App

The Movie Recommender App is a web application that recommends similar movies based on user input. It utilizes  cosine similarity matrix generated from the TMDB credits and movies datasets.

<br/>

## Features

- Recommends similar movies based on user input
- Displays movie details including title, overview, and poster image
- Provides an interactive and user-friendly interface

<br/>

## Getting Started

### _____________________________________________________

#### 1.Perform data analysis and generate the similarity matrix (sim_mat) and movie dictionary (movie_dict) as pickle files. Notebook should include the necessary code to load and preprocess the TMDB credits and movies datasets, calculate the similarity matrix, and create the movie dictionary.

<br/>

#### 2.Create a Python file (e.g., app.py) to define your Streamlit app. This file should include the necessary code to load the pickle files (sim_mat and movie_dict), define the layout and functionality of the app, and deploy it using the Streamlit library.

<br/>

#### 3.Create a setup.sh file to set up the required environment variables. 

<br/>

#### 4.Create a Proctfile file to specify the commands needed to run the app on Heroku. The Procfile should include the command to run the Streamlit app.

<br/>

#### 5.Generate a requirements.txt file that lists all the Python packages and their versions required for the project. You can generate this file using the pip freeze command in your project's virtual environment.

<br/>


## Configuration

Before running the app, ensure that you have set the following environment variable:

TMDB_API_KEY: Your API key for the TMDB API.
You can obtain an API key from the TMDB website (https://www.themoviedb.org/).