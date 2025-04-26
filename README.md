# 🎬 Movie Recommender System — Content-Based Filtering

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge)](https://content-based-movie-recommender-system-python-egywkb7tewyk2hfh.streamlit.app/)

🔗 **Live Demo:**  
👉 [Click to Try the App!](https://content-based-movie-recommender-system-python-egywkb7tewyk2hfh.streamlit.app/)

---

## 🚀 Introduction

Welcome to the **Movie Recommender App**!  
This application suggests similar movies based on user input using **content-based filtering** and **cosine similarity** — built entirely inside a **single `app.py`** without needing any heavy `.pkl` model files!

---

## ✨ Features

✅ Recommends movies based on your favorite movie 🎥  
✅ Displays movie titles and posters dynamically  
✅ Built with an interactive **Streamlit** frontend  
✅ Lightweight — No model files stored separately  
✅ Deploy-ready for **Streamlit Cloud** 🚀

---

## 🧠 How Does It Work?

1. **Data Collection**: Uses TMDB movie metadata (`movies.csv` and `credits.csv`).
2. **Feature Engineering**: Merges relevant fields like genres, cast, crew, keywords.
3. **Text Processing**: Cleans and processes text using NLP techniques.
4. **Vectorization**: Applies **Bag-of-Words** to feature columns.
5. **Similarity Computation**: Calculates **cosine similarity** between movies.
6. **Recommendation Logic**: Suggests top 5 similar movies based on the chosen movie.

---

## 🗂 Project Structure

| File/Directory    | Purpose                                   |
|-------------------|-------------------------------------------|
| `app.py`           | Main Streamlit application (single file). |
| `movies.csv`       | Movie metadata dataset.                  |
| `credits.csv`      | Credits information dataset.             |
| `requirements.txt` | Python dependencies list.                |

---

## 📂 Data Files

Since GitHub has file size limits, you can download the datasets directly:

- 📄 [movies.csv](https://drive.google.com/file/d/1V9dVf03-4B92vRv6TyI-LAFF4sNiEVRu/view?usp=drive_link)
- 📄 [credits.csv](https://drive.google.com/file/d/16T6VczZmXpjHqWhmJORHcHXiEJxPHaQO/view?usp=drive_link)

Move them into your project folder.

---

## 👨‍💻 Local Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

---

### 2️⃣ Install Dependencies
```bash
# Create a virtual environment
python -m venv env

# Activate
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

# Install packages
pip install -r requirements.txt
```

---

### 3️⃣ Add TMDB API Key
1. Create an account at [TMDB](https://www.themoviedb.org/).
2. Get your free API Key.
3. Inside `app.py`, replace:
```python
api_key = "your_api_key_here"
```
with your actual TMDB API key.

---

### 4️⃣ Run the Application
```bash
streamlit run app.py
```
🎉 Access the app at `http://localhost:8501/`

---

## 🌎 Deployment Instructions

### Deploy to **Streamlit Cloud**
1. Push the project to your GitHub repository.
2. Visit [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and deploy in minutes!

---

## 🎯 Tech Stack

- **Python** 🐍
- **Pandas**, **NumPy**
- **Scikit-learn** (for text vectorization)
- **Streamlit** (for frontend)
- **NLTK** (for text preprocessing)
- **Requests** (to fetch movie posters from TMDB API)

---

## 📈 Key Highlights

- Content-Based Filtering (NLP + Cosine Similarity)
- No need to upload heavy `.pkl` files.
- Poster images fetched live using TMDB API.
- Fast, efficient, and cloud deployable.

---

## 📣 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the movie data and API.
- Streamlit community for easy web app deployment.

---

🚀 **Happy Coding & Movie Watching!** 🍿🎬
