import requests
import os

from dotenv import load_dotenv

load_dotenv()


# OpenAI API Key
api_key = os.getenv('GPT_APIKEY')

def aiIMGExplainGPT(base64_image):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

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

                "temperature": "Provide the temperature range in degrees Celsius that the currunt plant is in. Example: 15°C",

                "humidity": "Give the humidity range in percentage that the currunt plant is in. Example: 40-60%",

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
                "text": 'Diagnose the img below and wrap your response in Curly brackets and dont put the word json infront of your response just give the json response'
            
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
    data = response.json()
    # data = response.json()["choices"][0]["message"]["content"]
    # print(data)
    return data