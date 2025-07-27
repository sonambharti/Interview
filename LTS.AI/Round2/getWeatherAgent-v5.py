# import httpx
import json
import requests
from datetime import datetime
from openai import OpenAI
import os

# Initialize OpenAI client with API key
# You can set your API key as an environment variable: OPENAI_API_KEY
# Or replace "YOUR_OPENAI_API_KEY" with your actual key
# api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
api_key = "Bearer YOUR_API_KEY"

# Check if API key is set
if api_key == "YOUR_OPENAI_API_KEY":
    print("❌ Error: OpenAI API key not set!")
    print("Please set your OpenAI API key in one of these ways:")
    print("1. Set environment variable: OPENAI_API_KEY=your_key_here")
    print("2. Replace 'YOUR_OPENAI_API_KEY' in the code with your actual key")
    exit(1)

client = OpenAI(api_key=api_key)

# Get user's question
question = input("How can i help you today?\n")

# Extract city name using OpenAI
try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that extracts city names from weather-related questions. You must respond with ONLY the city name, nothing else - no quotes, no punctuation, no additional text."
            },
            {
                "role": "user",
                "content": f"The user asked: {question}\n\nExtract just the city name from this weather question."
            }
        ],
        temperature=0.1,
        max_tokens=50
    )
    
    # Extract the city name from the response
    city_name = response.choices[0].message.content.strip()
    print(f"Extracted city: {city_name}")
    
except Exception as e:
    print(f"Error extracting city name: {e}")
    exit(1)

# Weather API configuration (using OpenWeatherMap API)
weather_api_key = "3f6b6e4d25a4a75d4fff9bce57a869c0"
  # Get from https://openweathermap.org/api
weather_url = f"http://api.openweathermap.org/data/2.5/weather"

# Get weather data
weather_params = {
    "q": city_name,
    "appid": weather_api_key,
    "units": "metric"  # Use Celsius
}

try:
    weather_resp = requests.get(weather_url, params=weather_params, timeout=10)
    weather_resp.raise_for_status()
    weather_data = weather_resp.json()
    
    # Extract weather information
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    
    # Format and display weather information
    print(f"\n🌤️  Weather for {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
    
except requests.exceptions.RequestException as e:
    print(f"Error getting weather data: {e}")
except KeyError as e:
    print(f"Error parsing weather data: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
