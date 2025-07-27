"""
Implement a post API to build an agent so that user can ask the weather of the places and agent should respond accordingly. After and beyond this it should say, " Sorry I am not able to answer this".
This only works for the word weather.
"""

import httpx
import re
# Replace with your actual OpenWeatherMap API key
OPENWEATHER_API_KEY = "YOUR_API_KEY"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
def extract_location(text: str) -> str | None:
    """
    Extract the location from a string like:
    'What is the weather in Paris?'
    """
    match = re.search(r"weather in ([a-zA-Z\s]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None
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
def run_agent():
    print("🤖 Hello! I can tell you the weather. Ask me something like 'What is the weather in Delhi?'\n(Type 'exit' to quit)\n")

    while True:
        query = input("You: ").strip()

        if query.lower() == "exit":
            print("Agent: Goodbye!")
            break

        if "weather in" in query.lower():
            location = extract_location(query)
            if location:
                response = get_weather(location)
                print(f"Agent: {response}")
            else:
                print("Agent: Please specify a valid location.")
        else:
            print("Agent: Sorry I am not able to answer this.")

if __name__ == "__main__":
    run_agent()


