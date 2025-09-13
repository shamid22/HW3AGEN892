import pandas as pd
import folium
import streamlit as st

# Set the page layout to wide (full width)
st.set_page_config(layout="wide")
with open("./income_map.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# Add a title for the page
st.title("State Income Map through the US")
st.components.v1.html(map_html, height=600, width=0,scrolling=True)
import pandas as pd
import streamlit as st
import os

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


# Create a DataFrame from the data
df = pd.DataFrame(leaderboard_data)

# Display the static table using st.table
# Note: st.table is best for small, static data as it's not interactive
st.table(df)

# --- Display a table of Markdown strings ---
st.header("Markdown Table Example")
st.markdown("This table demonstrates how `st.table` can render Markdown syntax directly within cells.")

# Sample data with Markdown strings
markdown_data = {
    'Feature': ['**Feature A**', '_Feature B_', '~~Feature C~~'],
    'Description': [
        'A key feature with a description.',
        'This feature is a good example.',
        'An example of a strike-through text.',
    ],
    'Link': [
        '[Learn More](https://www.streamlit.io)',
        'Check out [this link](https://docs.streamlit.io).',
        'No link here.',
    ]
}

# Create a DataFrame from the Markdown data
df_markdown = pd.DataFrame(markdown_data)

# Display the Markdown table using st.table
st.table(df_markdown)

st.info("The tables above are static representations of data. For larger, interactive datasets, consider using `st.dataframe`.")
