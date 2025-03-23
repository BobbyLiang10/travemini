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

st.title(":hotel: Hotel Finder")
st.sidebar.success("Choose one of our travel assistants!")
st.write("Hotel Finder helps you find the best hotels for your trip! Just input the city, the number of people staying per room, and how many nights you are staying. Then, sit back and watch as Hotel Finder recommends you five top-listed budget-friendly hotels just for you! Feel free to mention anything else to us and we will tailor our response to your request.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if (message["chat"]) == "hotels":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

##################
# Hotel Finder

# Prompt Template
input_prompt_hotel = """
You are an expert hotel planner and your job is to provide budget-friendly options to stay at the given location, unless explicitly mentioned.
Prioritize high ratings and hotels that are closer to the center of the location (city centre/downtown if possible).
Assume that there are two people per room, unless explicitly specified.
Recommend the top five hotels or AirBnbs with the above constraints or user constraints with the following details:
- Address of the hotel
- Rating out of 5 stars of the hotel
- Average cost per night at the hotel
- What people liked about the hotel (best reviews)
- Anything else that the user should be aware of while staying at this hotel
Give an emoji at the start of each point to better separate the responses.
Return the response using markdown with proper text formatting and styling.

"""

# Accepting user input
input_plan = st.chat_input("Input the city you wish to stay, the number of guests per room, and number of nights.")
if input_plan:
    st.session_state.messages.append({"chat": "hotels", "role": "user", "content": input_plan})
    with st.chat_message("user"):
        st.markdown(input_plan)

    response = get_response(input_prompt_hotel, input_plan)
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"chat": "hotels", "role": "assistant", "content": response})
    