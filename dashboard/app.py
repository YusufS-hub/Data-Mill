import streamlit as st
import pandas as pd
from src.transform import transformed_anime
import src.extract as e
from src.path import csv_file

path = csv_file
# Load and clean your data
csv_path = path  # adjust path if needed
df = e.extract_data(csv_path)
df = transformed_anime(df)

st.title("Anime Dashboard")

# Show the cleaned data
st.subheader("Cleaned Anime Data")
st.dataframe(df)

# Example: Genre distribution
if 'genre' in df.columns:
    st.subheader("Genre Distribution")
    st.bar_chart(df['genre'].value_counts())

# Example: Top rated anime
if 'rating' in df.columns and 'name' in df.columns:
    st.subheader("Top Rated Anime")
    top_rated = df.sort_values(by='rating', ascending=False).head(10)
    st.table(top_rated[['name', 'rating', 'genre']])