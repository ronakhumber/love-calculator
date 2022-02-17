import requests
import json
from pydantic import BaseModel, Field
from fastapi import Body, FastAPI

app = FastAPI()

class Names(BaseModel):
    mname:str
    fname:str

@app.post("/")
async def root(item: Names):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname":item.mname,"fname":item.fname}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "HEcEkXBA17mshuHUg34YWOOTCVg1p1SXS72jsnE1uUHuqLKmUz"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # return item;
    return json.loads(response.text)