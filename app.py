pip install streamlit google-generativeai python-dotenv pathlib

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
st.set_page_config(page_title = "Your personal AI Travel Assistant!")

st.title(":computer: Welcome to your personal AI travel agent!")
st.write("This website uses Google Gemini to help create a personal travel plan and all your travel needs to your destination!")

# Creating choices for user
section_choice = st.radio("Get started by choosing one of our assistants below!", ("Trip Planner", "Weather Bot", "Transport Bot", "Hotel Finder", "Restaurant Finder"))

#########

# Trip Planner
if section_choice == "Trip Planner":
    
    # Prompt Template
    input_prompt_planner = """
    You are a professional trip planner and your job is to provide a recommended plan for the user's inputted location
    given the number of days and the budget. 
    If the number of days and budget is not given, assume the trip is 3 days long
    and they have around $700 in local currency to spend.
    Prioritize hotels and restaurants that are top-rated, and include hidden gems that are worth visiting.
    Please include the budget of the hotel, restaurant, and attraction with each recommended place.
    Provide one interesting fact for each recommendation.
    Indicate the best month to visit for each attraction.
    Give an emoji for each point to better separate the locations and plans for each day.
    Return the response using markdown with proper text formatting and styling.
    """
    
    # Input
    input_plan = st.text_area("Input your location, number of days, and anticipated budget to obtain your personal itinerary!")
    
    # Button
    submit = st.button("Plan my trip!")
    if submit:
        response = get_response(input_prompt_planner, input_plan)
        st.subheader(":briefcase: Trip Planner Bot: ")
        st.write(response)
        
##################
# Weather Bot

if section_choice == "Weather Bot":
    
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
    
    Return the response using markdown.
    
    """
    
    # Input
    input_plan = st.text_area("Input your destination and find what the weather is like!")
    
    # Button
    submit = st.button("See weather forecast!")
    if submit:
        response = get_response(input_prompt_weather, input_plan)
        st.subheader(":sunny: Weather Bot: ")
        st.write(response)

##################
# Transport Bot

if section_choice == "Transport Bot":
    
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
    Return the response using markdown.
    """
    
    # Input
    input_plan = st.text_area("Indicate where you are travelling from and where your travel destination is.")
    
    # Button
    submit = st.button("Find transportation options!")
    if submit:
        response = get_response(input_prompt_transport, input_plan)
        st.subheader(":car: Transport Bot: ")
        st.write(response)
        

##################
# Hotel Finder

if section_choice == "Hotel Finder":
    
    # Prompt Template
    input_prompt_hotel = """
    You are an expert hotel planner and your job is to provide budget-friendly options to stay at the given location, unless explicitly mentioned.
    Prioritize high ratings and hotels that are closer to the center of the location (city centre/downtown if possible).
    Assume that there are two people per room, unless explicitly specified.
    Recommend the top five hotels or AirBnbs with the above constraints or user constraints with the following details:
    - Address of the hotel
    - Average cost per night at the hotel
    - What people liked about the hotel (best reviews)
    - Anything else that the user should be aware of while staying at this hotel
    - A link to the Google maps of where this hotel is located
    Give an emoji at the start of each point to better separate the responses.
    Return the response using markdown.
    
    """
    
    # Input
    input_plan = st.text_area("Input the city you are staying at, the number of guests, and the number of nights at the city.")
    
    # Button
    submit = st.button("Find your perfect hotel!")
    if submit:
        response = get_response(input_prompt_hotel, input_plan)
        st.subheader(":hotel: Hotel Finder: ")
        st.write(response)
        
        
#####################
# Restaurant Finder

if section_choice == "Restaurant Finder":
    
    # Prompt Template
    input_prompt_restaurant = """
    You are a professional food critic and your job is to provide the best restaurants given the location.
    Prioritize the restaurants by their top ratings and recommend what dishes the user should order from the restaurant.
    Categorize the restaurants in three price ranges: low, medium, and high, and recommend three restaurants per category.
    Give priority to local restaurants that you cannot find anywhere else in the world.
    List the average price of cuisine and dress code/style of the restaurant.
    Provide the address on where to find the restaurant.
    Give an emoji at the start of each point to better separate the responses.
    Return the response using markdown.
    
    """
    
    # Input
    input_plan = st.text_area("Type the city where you want me to find the best restaurants for!")
    
    # Button
    submit = st.button("Find my ideal restaurant!")
    if submit:
        response = get_response(input_prompt_restaurant, input_plan)
        st.subheader(":yum: Restaurant Finder: ")
        st.write(response)

