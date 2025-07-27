"""
Implement a post API to build an agent so that user can ask the weather of the places and agent should respond accordingly. After and beyond this it should say, " Sorry I am not able to answer this".
Use OPEN AI KEY to get the weather of the location.
"""

import httpx
# print("hello world")
question = input("How can i help you today?")

url = "https://api.openai.com/v1/responses"
headers = {
    "Authorization": f"Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}

payload = {
    "model": "gpt-4.1",
    "input": "The user is asking me for the weather of a city. help me extract just the city name.\n The user asked {question}\nYou will only output the city name and nothing else."
}

resp = httpx.post(url, headers=headers, json=payload, timeout=30)
resp.raise_for_status()
print(resp.json())
