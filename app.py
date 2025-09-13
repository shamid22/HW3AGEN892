import pandas as pd
import streamlit as st
import os
from numpy.random import default_rng as rng
# Set the page layout to wide (full width)
st.set_page_config(layout="wide")
# --- Display the Folium map from the HTML file ---
st.title("State Income Map through the US")
# Check if the map HTML file exists before trying to read it
if os.path.exists("./income_map.html"):
    with open("./income_map.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    # Display the map using the html component
    st.components.v1.html(map_html, height=600, width=0, scrolling=True)
else:
    st.error("Error: The file 'income_map.html' was not found. Please ensure it is in the same directory as this script.")
# --- Display a static table as a Leaderboard ---
st.header("Top Income States (Leaderboard)")
st.markdown("This static table displaying summaries top income static rankings ")

# Sample data for a small, static table
leaderboard_data = {
    'Rank': [1, 2, 3, 4, 5],
    'State': ['Massachusetts', 'California', 'New York', 'Washington', 'New Jersey'],
    'Median Household Income': ['$90,559', '$84,907', '$75,157', '$84,247', '$89,703'],
    'Change': ['+2.5%', '+1.8%', '+1.2%', '+2.1%', '+1.9%']
}
