"""
Implement a post API to build an agent so that user can ask the weather of the places and agent should respond accordingly. After and beyond this it should say, " Sorry I am not able to answer this".
"""

from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import re

app = FastAPI()

# Replace with your real OpenWeatherMap API key
OPENWEATHER_API_KEY = "YOUR_API_KEY"  # replace with YOUR_API_KEY
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

# Request schema
class QueryRequest(BaseModel):
    query: str
  
def extract_location(text: str) -> str | None:
    """
    Extract the location from a query string like:
    'What is the weather in Paris?'
    """
    match = re.search(r"weather in ([a-zA-Z\s]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None
  
@app.post("/agent/weather")
async def weather_agent(request: QueryRequest):
    query = request.query.strip()
    # Check if it's a weather query
    if "weather in" in query.lower():
        location = extract_location(query)
        if location:
            async with httpx.AsyncClient() as client:
                params = {
                    "q": location,
                    "appid": OPENWEATHER_API_KEY,
                    "units": "metric"
                }
                response = await client.get(WEATHER_URL, params=params)
                if response.status_code == 200:
                    data = response.json()
                    weather = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]
                    return {
                        "response": f"The weather in {location.title()} is {weather} with a temperature of {temperature}°C."
                    }
                else:
                    return {"response": f"Sorry, I couldn't fetch weather data for {location.title()}."}
        else:
            return {"response": "Please specify a location to check the weather."}
    # Fallback response for any non-weather query
    return {"response": "Sorry I am not able to answer this."}
