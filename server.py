from fastapi import FastAPI
import requests
import json

app = FastAPI()


@app.post("/")
async def root():
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":"Alice","fname":"John"}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "HEcEkXBA17mshuHUg34YWOOTCVg1p1SXS72jsnE1uUHuqLKmUz"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return json.loads(response.text)