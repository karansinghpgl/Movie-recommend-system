# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit. It recommends the top 5 similar movies based on the movie selected by the user.

## 🚀 Live Demo
[Click here to view the application](https://movie-recommend-system-bt6xwgkbcex7bhvxn7ukbw.streamlit.app/)

## 📌 Project Overview
This project uses Content-Based Filtering to recommend movies based on their similarity.

When a user selects a movie, the system calculates similarity scores and displays the top 5 recommended movies.

## ✨ Features
- Select your favourite movie from a dropdown menu.
- Get the top 5 similar movie recommendations.
- Display movie posters with recommendations.
- Interactive web interface built using Streamlit.
- Content-Based Filtering using Cosine Similarity.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- TMDB Movie Dataset

## 📂 Project Structure

```text
Movie-recommend-system/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── movierec.ipynb
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/karansinghpgl/Movie-recommend-system.git
```

**2. Navigate to the project folder**

```bash
cd Movie-recommend-system
```

**3. Install dependencies**

```bash
pip install streamlit pandas numpy scikit-learn requests
```

**4. Run the application**

```bash
streamlit run app.py
```

## 🧠 How It Works

1. Movie information is processed using Pandas.
2. Text features are combined into tags.
3. CountVectorizer converts text into numerical vectors.
4. Cosine Similarity measures similarity between movies.
5. The system returns the top 5 most similar movies.

## 📊 Dataset
The project uses the TMDB 5000 Movie Dataset containing movie details, genres, keywords, cast, and crew.

## 👨‍💻 Author
**Karan Singh**

- GitHub: https://github.com/karansinghpgl
- LinkedIn: https://linkedin.com/in/karan-singh-7046b1372

---

⭐ If you like this project, feel free to star the repository!
