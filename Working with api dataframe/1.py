import requests

url = "https://linkedin-api8.p.rapidapi.com/similar-profiles"

querystring = {
    "url": "https://www.linkedin.com/in/williamhgates/"
}

headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
}

response = requests.get(
    url,
    headers=headers,
    params=querystring
)

print(response.json())