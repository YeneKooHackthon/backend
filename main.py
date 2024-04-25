from fastapi import FastAPI, UploadFile, File
from inference import inFerence
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(provider: str = None,  plant: str = None, file: UploadFile = File(...)):
    return await inFerence(plant, file, provider)