
import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommendation function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Fetch movie poster
@st.cache_data(show_spinner=False)
def fetch_poster(movie_name):

    url = "https://api.streamx.qzz.io/search"

    params = {
        "q": movie_name,
        "type": "movie"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        for item in data.get("metas", []):

            poster = item.get("poster")

            if poster:
                return poster

    except requests.RequestException:
        return None

    except ValueError:
        return None

    return None


# Streamlit UI
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    "Select Your Favourite Movie",
    movies['title'].values
)


if st.button("Recommend"):

    recommendations = recommend(selected_movie_name)

    st.subheader("Recommended Movies")

    # Display posters in columns
    cols = st.columns(5)

    for i, movie in enumerate(recommendations):

        with cols[i]:

            poster = fetch_poster(movie)

            st.write(movie)

            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.write("Poster not available")



















































































