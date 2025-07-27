"""
Implement a post API to build an agent so that user can ask the weather of the places and agent should respond accordingly. After and beyond this it should say, " Sorry I am not able to answer this".
Created small NLU layer to identify the keyword word.
"""

import httpx
import re

# ----------- Simulated NLU Layer -------------
def detect_intent(text: str) -> str:
    """
    Simulate intent detection using keyword rules.
    Returns 'get_weather' or 'unknown'
    """
    weather_keywords = [
        "weather", "hot", "cold", "temperature", "climate", "rain",
        "raining", "umbrella", "humid", "snow", "sunny", "windy"
    ]
    text_lower = text.lower()
    if any(word in text_lower for word in weather_keywords):
        return "get_weather"
    return "unknown"

def extract_entities(text: str) -> dict:
    """
    Extract location entities using regex patterns.
    Returns a dict like {'location': 'Delhi'}
    """
    patterns = [
        r"in ([a-zA-Z\s]+)",
        r"at ([a-zA-Z\s]+)",
        r"about ([a-zA-Z\s]+)",
        r"for ([a-zA-Z\s]+)",
        r"([A-Z][a-z]+(?: [A-Z][a-z]+)*)$"   # Matches "New York", "Paris"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return {"location": match.group(1).strip()}
    return {}

# ----------- Weather Fetching Logic -------------
OPENWEATHER_API_KEY = "YOUR_API_KEY"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(location: str) -> str:
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }
    try:
        response = httpx.get(WEATHER_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"The weather in {location.title()} is {weather} with a temperature of {temperature}°C."
        else:
            return f"Sorry, I couldn't fetch weather data for {location.title()}."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# ----------- Main Driver -------------
def main():
    query = input("Enter your query: ").strip()

    intent = detect_intent(query)
    entities = extract_entities(query)

    if intent == "get_weather" and "location" in entities:
        location = entities["location"]
        print(get_weather(location))
    else:
        print("Sorry I am not able to answer this.")

if __name__ == "__main__":
    main()
