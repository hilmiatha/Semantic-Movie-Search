import streamlit as st
from movies import moviesdb


movies = moviesdb()
db = movies.load_db()


st.title('Semantic Movie Search :popcorn:')
movie_description = st.text_input("Write the movie description", value="")

    
movies = movies.get_movies(db, movie_description)


if st.button("Get the closest movies.", ):
    for i in movies:
        st.success(f"Movie Name: {i.metadata['title']}", icon= "🎬")
        st.success(f"Movie Description: {i.page_content}", icon= "📜")
