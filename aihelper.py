import google.generativeai as genai
import textwrap
import json

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GEMINI_APIKEY')

genai.configure(api_key=GOOGLE_API_KEY)


imgModel = genai.GenerativeModel('gemini-pro-vision')

textModel = genai.GenerativeModel('gemini-pro')


def to_markdown(text):
    texta = text.replace('•', '  *')
    textl = texta.replace('```', '')
    return textwrap.indent(textl, ' ', predicate=lambda _: True)


def promptText(plant_name):
    messages = f'''
    You are a vital agricultural expert in Ethiopia, specializing in detecting and classifying plant diseases to safeguard crops and ensure a sustainable agricultural ecosystem. Here's how to structure your responses:

    plant_name: Provide the name of the plant.

    common_name: Provide common name of the plant

    genus: Provide its genus of the plant


    scientific_name: Provide scientific name of the plant

    status: Respond with "red" if the plant is unhealthy, and "green" if it's healthy.

    disease: The name of the disease if the plant is unhealthy else responde Healthy: Example: Rust, Healthy etc

    description:Briefly describe the plant species and its agricultural use also Elaborate on its use case for health. (A Minimum 80 words) 

    causes: Explain the disease affecting the plant, its causes. Guide farmers on how to effectively identify and diagnose the issue. (List 3)

    symptoms: Explain the plant's disease observable symptoms. Guide farmers what is visible on the plant. (List 3)

    prevention_or_treatment_mechanisms: Offer expert recommendations for preventing disease spread or implementing effective treatment strategies. Focus on sustainable practices to promote long-term plant health and ecosystem resilience. (List 3 mechanisms)

    temperature: Provide the temperature range in degrees Celsius that the plant thrives in. Example: 15°C

    humidity: Give the humidity range in percentage suitable for the plant. Example: 40-60%

    Approach each response as though you're advising a fellow agricultural expert, offering actionable advice based on your deep understanding of plant pathology and agricultural best practices. Remember, answer as your are a {plant_name}, and your expertise is crucial for its vitality and productivity in the agricultural sector.

    !NOTICE: force your response to be in JSON 
    '''

    return messages


def textPrompt(txt, context):
    messages = [
        {"role": "user", "parts": "Explain about your self"},
        {"role": "model", "parts": "I am a helpful Ethiopian agricaltural assistant my main focus is on plant disease ditection and calssiffication then i will give this 3 response  one overview discription abour the plnat type name and usecase, second what is the cause if the plant is affected and 3rd prevention or treatment mechanisim for the better health of the plant"},
        {"role": "user", "parts": "who are you?"},
        {"role": "model", "parts": "I'm your Agri assistant created by YeneKoo called GebereKoo."},
        {"role": "user", "parts": "who developed you."},
        {"role": "model", "parts": "I have been developed by a team of agricultural experts and software engineers at YeneKoo, an Ethiopian-based technology company."},
        {"role": "user", "parts": 'context: ' + context + '\nquestion: ' + txt}
    ]
    return messages


def aiIMGExplain(img_binnary, plant_name):
    plant_picture = {
        'mime_type': 'image/png',
        'data': img_binnary
    }

    response = imgModel.generate_content(
        contents=[promptText(plant_name), plant_picture]
    )
    json_string = to_markdown(response.text).replace("  json\n", "")

    data = json.loads(json_string)
    print(response.text)
    return data


def aiTextExplain(txt, context):
    response = textModel.generate_content(textPrompt(txt, context))
    return response.text
