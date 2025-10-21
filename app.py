# Import the libraries
import os
import google.generativeai as genai
import streamlit as st
from utils import get_api_key

# Configure API key (prefers Streamlit secrets -> env)
genai.configure(api_key=get_api_key())

# Function to load Google Gemini Model
def get_response(prompt, input):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt, input])
    return response.text

# Page setup
planner_page = st.Page(
    page="pages/planner.py",
    title="Trip Planner",
    icon="💼",
    default = True
)

weather_page = st.Page(
    page="pages/weather.py",
    title="Weather Bot",
    icon="🌤"
)

transport_page = st.Page(
    page="pages/transport.py",
    title="Transport Bot",
    icon="🚌"
)

hotels_page = st.Page(
    page="pages/hotels.py",
    title="Hotel Finder",
    icon="🏨"
)

restaurants_page = st.Page(
    page="pages/restaurants.py",
    title="Restaurant Finder",
    icon="😋"
)

pg = st.navigation(pages=[planner_page, weather_page, transport_page, hotels_page, restaurants_page])

pg.run()
