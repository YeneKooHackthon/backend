from fastapi import FastAPI, UploadFile, File
from inference import inFerence


app = FastAPI()

@app.get("/sms")
def main(): #use the twilio.py file
    return 'abcd'

@app.post("/predict")
async def predict(plant: str = None, file: UploadFile = File(...)):
    return await inFerence(plant, file)