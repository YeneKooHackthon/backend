import requests
import os

from dotenv import load_dotenv

load_dotenv()


GPT_API_KEY = os.getenv('GPT_APIKEY')

# OpenAI API Key
api_key = GPT_API_KEY

# Getting the base64 string

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

def aiIMGExplainGPT(base64_image):
    payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {"role": "system", "content": 
        '''
            You are a vital agricultural expert in Ethiopia, specializing in detecting and classifying plant diseases to safeguard crops and ensure a sustainable agricultural ecosystem. Here's how to structure your responses:
        {
            "plant_name": "Provide the name of the plant.",

            "common_name": "Provide common name of the plant",

            "genus": "Provide its genus of the plant",


            "scientific_name": "Provide scientific name of the plant",

            "status": "Respond with "red" if the plant is unhealthy, and "green" if it's healthy.",

            "disease": "The name of the disease if the plant is unhealthy else responde Healthy: Example: Rust, Healthy etc",

            "description": "Briefly describe the plant species and its agricultural use also Elaborate on its use case for health. (A Minimum 80 words)", 

            "causes": "Explain the disease affecting the plant, its causes. Guide farmers on how to effectively identify and diagnose the issue. (List 3)",

            "symptoms": "Explain the plant's disease observable symptoms. Guide farmers what is visible on the plant. (List 3)",

            "prevention_or_treatment_mechanisms": "Offer expert recommendations for preventing disease spread or implementing effective treatment strategies. Focus on sustainable practices to promote long-term plant health and ecosystem resilience. (List 3 mechanisms)",

            "temperature": "Provide the temperature range in degrees Celsius that the plant thrives in. Example: 15°C",

            "humidity": "Give the humidity range in percentage suitable for the plant. Example: 40-60%",

        }
        Approach each response as though you're advising a fellow agricultural expert, offering actionable advice based on your deep understanding of plant pathology and agricultural best practices. Remember, answer as your are an expert, and your expertise is crucial for its vitality and productivity in the agricultural sector.

        !NOTICE: force your response to be in JSON 
        '''
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": 'Diagnose the img below'
        
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Parse the JSON string into a Python dictionary
    data = response.json()["choices"][0]["message"]["content"]
    # print(data)
    return data