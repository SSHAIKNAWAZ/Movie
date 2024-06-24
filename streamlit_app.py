import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    try:
        response = requests.get(url=f'https://api.themoviedb.org/3/movie/{movie_id}'
                                    f'?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if 'poster_path' in data and data['poster_path'] is not None:
            return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
        else:
            st.warning(f"No poster found for movie ID {movie_id}")
            return None  # Return None if no poster URL is found
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
        return None  # Handle request exceptions
    except (KeyError, ValueError) as e:
        st.error(f"Error parsing API response: {e}")
        return None  # Handle JSON parsing errors


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# Load data and similarity matrix
movie_dict = pickle.load(open('movie_dict_copy.pk', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity_copy.pk', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Enter the Movie Name', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col = st.columns(5)
    for i in range(5):
        with col[i]:
            st.text(names[i - 1])
            if posters[i - 1] is not None:
                st.image(posters[i - 1])
            else:
                st.warning("No poster available")

    # col1,col2,col3,col4,col5=st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    #
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    #
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    #
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    #
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
    #
