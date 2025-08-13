
import streamlit as st
import pandas as pd
import plotly.express as px

# Use relative imports for dashboard context
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from transform import transformed_anime
import extract as e
from path import csv_file

# -------------------
# Load and clean data
# -------------------
csv_path = csv_file
df = e.extract_data(csv_path)
df = transformed_anime(df)

# Ensure correct types and handle missing columns
if 'rating' in df.columns:
    df['rating'] = df['rating'].astype(str).str.replace('/10', '', regex=False).replace('', pd.NA).astype(float)
else:
    df['rating'] = pd.NA
if 'members' in df.columns:
    df['members'] = df['members'].astype(str).str.replace(',', '', regex=False).str.replace(' members', '', regex=False).replace('', pd.NA).astype(float)
else:
    df['members'] = pd.NA
if 'genre' in df.columns:
    df['genre'] = df['genre'].astype(str).str.strip()
else:
    df['genre'] = ''
if 'name' not in df.columns:
    df['name'] = df.index.astype(str)

# -------------------
# Sidebar Filters
# -------------------
st.sidebar.header("🔍 Filters")
all_genres = sorted(set(g.strip() for sublist in df['genre'].dropna().str.split(',') for g in sublist if g.strip()))
selected_genres = st.sidebar.multiselect("Select Genres", all_genres)
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 7.0)
search_term = st.sidebar.text_input("Search by Name")

# Filter logic
filtered_df = df[df['rating'].fillna(0) >= min_rating]
if selected_genres:
    filtered_df = filtered_df[filtered_df['genre'].apply(lambda g: any(sg in g for sg in selected_genres))]
if search_term:
    filtered_df = filtered_df[filtered_df['name'].str.contains(search_term, case=False, na=False)]

# -------------------
# Dashboard Header
# -------------------
st.title("🎯 Anime Dashboard")
st.caption("Powered by ETL pipeline data")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("📺 Total Anime", len(filtered_df))
col2.metric("⭐ Avg Rating", f"{filtered_df['rating'].mean():.2f}" if not filtered_df['rating'].isna().all() else "N/A")
col3.metric("👥 Total Members", f"{int(filtered_df['members'].sum()):,}" if not filtered_df['members'].isna().all() else "N/A")

# -------------------
# Charts
# -------------------
# Genre Distribution
st.subheader("📊 Genre Distribution")
genre_counts = pd.Series([g.strip() for sublist in filtered_df['genre'].dropna().str.split(',') for g in sublist if g.strip()]).value_counts()
if not genre_counts.empty:
    fig_genres = px.bar(x=genre_counts.index, y=genre_counts.values, labels={'x': 'Genre', 'y': 'Count'})
    st.plotly_chart(fig_genres, use_container_width=True)
else:
    st.info("No genre data available for selected filters.")

# Top Rated Anime
st.subheader("🏆 Top Rated Anime")
if 'rating' in filtered_df.columns and 'name' in filtered_df.columns:
    top_rated = filtered_df.sort_values(by='rating', ascending=False).head(10)
    if not top_rated.empty:
        fig_top = px.bar(top_rated, x='name', y='rating', color='genre', title="Top 10 Anime by Rating")
        st.plotly_chart(fig_top, use_container_width=True)
    else:
        st.info("No top rated anime available for selected filters.")

# -------------------
# Data Table
# -------------------
st.subheader("📄 Anime Data")
st.dataframe(filtered_df)

# -------------------
# Detail View
# -------------------
st.subheader("🔍 Anime Details")
if not filtered_df.empty:
    selected_anime = st.selectbox("Select Anime", filtered_df['name'].unique())
    anime_row = filtered_df[filtered_df['name'] == selected_anime].iloc[0]
    st.markdown(f"**Name:** {anime_row['name']}")
    st.markdown(f"**Genres:** {anime_row['genre']}")
    st.markdown(f"**Type:** {anime_row.get('type', 'N/A')}")
    st.markdown(f"**Episodes:** {anime_row.get('episodes', 'N/A')}")
    st.markdown(f"**Rating:** {anime_row.get('rating', 'N/A')}")
    st.markdown(f"**Members:** {anime_row.get('members', 'N/A')}")
