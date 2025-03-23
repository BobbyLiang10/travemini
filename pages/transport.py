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

st.title(":car: Transport Bot")
st.sidebar.success("Choose one of our travel assistants!")
st.write("Transport Bot helps determine the best method of transportation from point A to point B! Just input your origin and destination and Transport Bot will consider all modes of transportation and determine the most optimal time and cost efficient way of travelling!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    if (message["chat"]) == "transport":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#########

# Prompt Template
    input_prompt_transport = """
    You are a professional transportation analyst and your job is to find the most efficient and cost-effective way to get from one place to another. 
    Please indicate all modes of travel to the desired destination, including walking, cycling, scooter, and taxi options if applicable.
    If the walking distance is more than one hour, don't display this as one of your options.
    If it takes more than 30 minutes for scooter and cycling options, do not include this in your analysis, unless the user specifically mentions this option.
    If the transportation is public, include the frequency and timetable of the transportation schedule.
    Prioritize cost and time into your analysis.
    Please include the website URL to purchase any tickets required.
    Please include the cost and time for each mode of transport.
    Also indicate if the route is drivable, assume the user has a car and list the fuel consumption price per day. 
    If the user did not indicate that they have a car, include car rental prices per day.
    Create a summary table comparing the options listed.
    At the end of your response, provide your ultimate recommendation and sample travel plan factoring in the above constraints and provide the total cost of transportation to get there.
    Give an emoji at the start of each point to better separate the responses.
    Return the response using markdown with proper text formatting and styling.
    """
    
# Input
input_plan = st.chat_input("Where do you want to go?")
if input_plan:
    st.session_state.messages.append({"chat": "transport", "role": "user", "content": input_plan})
    with st.chat_message("user"):
        st.markdown(input_plan)

    response = get_response(input_prompt_transport, input_plan)
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"chat": "transport", "role": "assistant", "content": response})