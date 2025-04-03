# 🎬 Movie Recommender App - Step-by-Step Guide

Welcome to the **Movie Recommender App**! This guide will help you set up and run the application locally. The app suggests similar movies based on user input using a **cosine similarity matrix** generated from the TMDB (The Movie Database) dataset.

---

## ✨ Features

✅ Recommends movies based on user input.  
✅ Displays movie details (title, overview, and poster image).  
✅ Provides an interactive, user-friendly interface using **Streamlit**.  

---

## 📝 Theoretical Understanding

### 🔍 How Does It Work?
1. **Data Collection:** The app uses the TMDB dataset, which includes movie metadata and credits.
2. **Feature Extraction:** Important features like genres, cast, and crew are extracted.
3. **Text Processing & Vectorization:** A similarity matrix is created using the **cosine similarity** metric.
4. **Recommendation Algorithm:** Given a movie title, the app finds the most similar movies using the precomputed similarity matrix.

---

## 👨‍💻 Setup & Installation

Follow these steps to run the app locally:

### ➕ Step 1: Clone the Repository
```bash
# Clone the project repository
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

---

### ➕ Step 2: Install Dependencies
Create a virtual environment and install the required Python libraries.
```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### ➕ Step 3: Set Up TMDB API Key
Register on [TMDB](https://www.themoviedb.org/) and get your API key.
Create a **.env** file in the root directory and add:
```env
TMDB_API_KEY=your_api_key_here
```

---

### ➕ Step 4: Prepare Data Files
🔄 **Download & Save the Required Files**
Since GitHub has a file size limit of 25MB, we need to download the required `.pkl` files manually.

#### **Download Links:**
- 🔒 [movie_dict.pkl](https://drive.google.com/uc?export=download&id=1agHhtrmIQ4i4B-dhyuH8ryAWtZAon-SW)
- 🔒 [sim_mat.pkl](https://drive.google.com/uc?export=download&id=1EbEPHAn-2ONVw5_nqEbglQxEYi5GZgs7)

🛠 **Move the files** to the project folder.
```bash
mv ~/Downloads/movie_dict.pkl ./
mv ~/Downloads/sim_mat.pkl ./
```

---

### ➕ Step 5: Run the App
🎉 Now, let's start the Streamlit app!
```bash
streamlit run app.py
```

---

## 🌟 Files & Directories Explained

| File/Directory   | Description |
|-----------------|-------------|
| `app.py`        | Main application script. |
| `movie_dict.pkl`| Precomputed movie dictionary. |
| `sim_mat.pkl`   | Precomputed similarity matrix. |
| `requirements.txt` | List of dependencies. |
| `setup.sh`      | Environment setup script. |
| `Procfile`      | Defines commands for deployment. |

---

## 🚀 Deployment (Optional)
If you want to deploy the app, you can use **Streamlit Cloud** or **Heroku**.

### **🌐 Deploy on Streamlit Cloud**
1. Push your code to a **public GitHub repo**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and deploy your repo.

### **🛠 Deploy on Heroku**
1. Install Heroku CLI:
```bash
pip install heroku
```
2. Create a `Procfile`:
```bash
echo "web: streamlit run app.py" > Procfile
```
3. Deploy:
```bash
git init
git add .
git commit -m "Deploy"
heroku create your-app-name
git push heroku master
heroku open
```

---

## 🌟 Conclusion
Congratulations! You have successfully set up the **Movie Recommender App** on your local machine. Now, you can explore movie recommendations and experiment with different datasets.


🚀 **Happy Coding & Movie Watching!** 🍿🎬
