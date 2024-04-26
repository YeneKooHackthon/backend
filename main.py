import requests
from fastapi import FastAPI, UploadFile, File
from inference import inFerence
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv


app = FastAPI()

load_dotenv()

UNSPLASH_KEY = os.getenv('UNSPLASH_KEY')

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/plant/img')
async def fetch_data(plant: str = "plant"):
    url = f'https://api.unsplash.com/search/photos?client_id={UNSPLASH_KEY}&query=${plant}-plant&per_page=5'

    url_array = []
    response = requests.get(url)
    data = response.json()
    # print('data', data)

    # Assuming data structure matches what is expected
    for result in data['results']:
        full_url = result['urls']['full']
        url_array.append(full_url)

    return url_array




@app.post("/predict")
async def predict(provider: str = None,  plant: str = None, file: UploadFile = File(...)):
    return await inFerence(plant, file, provider)