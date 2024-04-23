import onnxruntime
import numpy as np
from PIL import Image
import io
from aihelper import aiIMGExplain

import base64


# Load the ONNX model
onnx_model = {
        'corn_onnx_model': onnxruntime.InferenceSession('./assets/models/best_model_bokolo.onnx')
    }

img_height, img_width = 150, 150


# trained_models
custom_trained_models = ['corn']

# Define class labels
class_labels = {
        "corn": ['blight', 'common_rust', 'gray_leaf_spot', 'healthy']
    }


# Get predicted class label
def predctionClassname(plant_name ,prediction):
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[plant_name][predicted_class_index]
    return predicted_class


# Run inference
def modelPredction(plant_name, img_array):
    input_name = onnx_model['corn_onnx_model'].get_inputs()[0].name
    output_name = onnx_model['corn_onnx_model'].get_outputs()[0].name
    prediction = onnx_model['corn_onnx_model'].run([output_name], {input_name: img_array.astype(np.float32)})[0]
    return predctionClassname(plant_name ,prediction)    



async def inFerence(plant_name, file, provider):
    contents = await file.read() # Read the image file from the request
    if plant_name in custom_trained_models:
        image = Image.open(io.BytesIO(contents)).resize((img_height, img_width))
        img_array = np.array(image)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Normalize the image
        ai_res = modelPredction(plant_name, img_array) 
        
        return {"predicted_class": ai_res}

    img_data = base64.b64encode(contents).decode('utf-8')
    return  aiIMGExplain(img_data, provider = provider)
