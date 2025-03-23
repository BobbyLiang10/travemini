import streamlit as st

# Import the libraries
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Load API key
load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model
def get_response(prompt, input):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt, input])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title = "Travemini, your AI Travel Agent.")

st.title(":briefcase: Welcome to Travemini, your personal AI Travel agent!")
st.sidebar.success("Choose one of our travel assistants!")
st.write("Travemini uses Google Gemini to help create a personal travel plan and provide travel tips for your destination!")
st.write("To start, input your location, number of days, and anticipated budget to obtain your personal itinerary. Feel free to include any other information to our bot and we will gladly tailor our response to your request.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    if (message["chat"]) == "planner":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#########

# Trip Planner
# Prompt Template
input_prompt_planner = """
You are a professional trip planner and your job is to provide a recommended plan for the user's inputted location
given the number of days and the budget.
If the number of days and budget is not given, assume the trip is 3 days long
and they have around $700 in USD equivalent of local currency to spend.
Prioritize hotels and restaurants that are top-rated, and include hidden gems that are worth visiting.
Please include the budget of the hotel, restaurant, and attraction with each recommended place.
Provide one interesting fact for each recommendation.
Indicate the best month to visit for each attraction.
Give an emoji for each point to better separate the locations and plans for each day.
Return the response using markdown with proper text formatting and styling.
"""
# Input
input_plan = st.chat_input("Input your location, number of days, and anticipated budget.")
if input_plan:
    st.session_state.messages.append({"chat": "planner", "role": "user", "content": input_plan})
    with st.chat_message("user"):
        st.markdown(input_plan)

    response = get_response(input_prompt_planner, input_plan)
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"chat": "planner", "role": "assistant", "content": response})