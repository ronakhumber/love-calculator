import requests
import json
from pydantic import BaseModel, Field
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://localhost:5500/cf.html",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Names(BaseModel):
    mname:str
    fname:str
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

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