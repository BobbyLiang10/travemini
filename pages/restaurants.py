import streamlit as st

# Import the libraries
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st
from utils import get_api_key

# Configure API key
genai.configure(api_key=get_api_key())

# Function to load Google Gemini Model
def get_response(prompt, input):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt, input])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title = "Travemini, your AI Travel Agent.")

st.title(":yum: Restaurant Finder")
st.sidebar.success("Choose one of our travel assistants!")
st.write("Restaurant Finder helps determine the most delicious cuisines in your area! Just input your destination and Restaurant Finder will find you the best culinary tastes the area has to offer. Eating on a budget or fancying fine dining? Restaurant Finder will provide three restaurants for each price category and recommend their best-selling dishes! Feel free to tell us what types of cuisine you are craving and our bot will find something that matches your taste buds!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    if (message["chat"]) == "restaurant":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#########

# Prompt Template

input_prompt_restaurant = """
    You are a professional food critic and your job is to provide the best restaurants given the location.
    Prioritize the restaurants by their top ratings and recommend what dishes the user should order from the restaurant.
    Categorize the restaurants in three price ranges: low, medium, and high, and recommend three restaurants per category.
    Give priority to local restaurants that you cannot find anywhere else in the world.
    List the average price of cuisine and dress code/style of the restaurant.
    Provide the address on where to find the restaurant.
    Give an emoji at the start of each point to better separate the responses.
    Return the response using markdown with proper text formatting and styling.
    
    """
    
# Input
input_plan = st.chat_input("Give me a location and I'll find you the best food in the area!")
if input_plan:
    st.session_state.messages.append({"chat": "restaurant", "role": "user", "content": input_plan})
    with st.chat_message("user"):
        st.markdown(input_plan)

    response = get_response(input_prompt_restaurant, input_plan)
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"chat": "restaurant", "role": "assistant", "content": response})