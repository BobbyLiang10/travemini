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

st.title(":sunny: Weather Bot")
st.sidebar.success("Choose one of our travel assistants!")
st.write("Weather Bot provides you an estimate on how the weather will be like at your destination! Just enter a destination and time frame, and Weather Bot will return the historical average and type of weather you can expect at your location. Weather Bot will also provide any clothing suggestions depending on the weather, you'll no longer have to think about what types of clothes to pack!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    if (message["chat"]) == "weather":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#########

# Prompt Template
    # Prompt Template
input_prompt_weather = """
    You are a professional weather forecaster.
    Your job is to provide a weather forecast given the location, listing the forecast for the next 7 days from the current date, unless explicitly specified.
    Please also indicate that these are historical averages and are used for reference only.
    Please list the following in your forecast, within a table:
    - Temperature
    - Wind speed
    - Hours of sunlight
    - Amount of precipitation
    - Air Quality Index (in simple terms)
    
    Please also provide the link to where the data is being retrieved from.
    Indicate what type of clothing the user should wear and prepare for the weather.
    Return the response using markdown with proper text formatting and styling.
    
    """
    
# Input
input_plan = st.chat_input("Enter a location.")
if input_plan:
    st.session_state.messages.append({"chat": "weather", "role": "user", "content": input_plan})
    with st.chat_message("user"):
        st.markdown(input_plan)

    response = get_response(input_prompt_weather, input_plan)
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"chat": "weather", "role": "assistant", "content": response})