import streamlit as st
import joblib
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Movie Genre Predictor",
    page_icon="🎬",
    layout="wide"
)

model = joblib.load("model/genre_model.pkl")
tfidf = joblib.load("model/tfidf.pkl")

st.markdown("""
# 🎬 AI Movie Genre Predictor

Predict movie genres using NLP and Machine Learning.
""")

col1, col2 = st.columns([2,1])

with col1:

    movie_plot = st.text_area(
        "Enter Movie Plot",
        height=250
    )

    if st.button("Predict Genre 🚀"):

        vector = tfidf.transform([movie_plot])

        prediction = model.predict(vector)[0]

        st.success(
            f"Predicted Genre: {prediction.upper()}"
        )

with col2:

    st.image(
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",
        use_container_width=True
    )

st.divider()

genres = [
    "Drama",
    "Comedy",
    "Action",
    "Thriller",
    "Horror",
    "Romance",
    "Adventure"
]

df = pd.DataFrame({
    "Genre": genres,
    "Popularity": [90,85,80,70,65,75,60]
})

fig = px.bar(
    df,
    x="Genre",
    y="Popularity",
    title="Popular Genres",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
