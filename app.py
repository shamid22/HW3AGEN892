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
st.markdown("This is a small, static table displaying key metrics")

# Sample data for a small, static table
leaderboard_data = {
    'Rank': [1, 2, 3, 4, 5],
    'State': ['Massachusetts', 'California', 'New York', 'Washington', 'New Jersey'],
    'Median Household Income': ['$90,559', '$84,907', '$75,157', '$84,247', '$89,703'],
    'Change': ['+2.5%', '+1.8%', '+1.2%', '+2.1%', '+1.9%']
}

# Create a DataFrame from the data
df_leaderboard = pd.DataFrame(leaderboard_data)

# Display the static table using st.table
# Note: st.table is best for small, static data as it's not interactive
st.table(df_leaderboard)

# --- Display a table of random numbers ---
st.header("Random Number Table Example")
st.markdown("This table demonstrates a static table with randomly generated data.")

# Create a DataFrame with random data and new, more descriptive columns
df_random = pd.DataFrame(
    rng(0).standard_normal(size=(10, 5)),
    columns=['Feature 1 (Avg)', 'Feature 2 (Max)', 'Feature 3 (Min)', 'Feature 4 (StdDev)', 'Feature 5 (Variance)'],
)

# Display the random data table
st.table(df_random)

st.info("The tables above are static representations of data. For larger, interactive datasets, consider using `st.dataframe`.")
