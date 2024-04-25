import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application, MessageHandler, filters
from telegram.constants import ParseMode
import requests
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = ""
with open("token.txt", 'r') as file:
    TOKEN = file.read()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_message = f"""Hello <b>{update.effective_user.first_name or update.effective_user.username}</b>
    this is <a><b><i>geberekoo</i></b></a> send me photo of a plant and i will send you the analysis of the plant

    use <a>/help</a> for more detail
    """
    with open("users.txt", 'a', encoding='utf-8') as users:
        users.write((update.effective_user.username or '') + ',' + (update.effective_user.first_name or '') + '\n')

    await update.message.reply_text(start_message, parse_mode=ParseMode.HTML)



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = f"""Hello <b>{update.effective_user.first_name or update.effective_user.username}</b>,

This is the <a href="https://geberekoo.pages.dev/"><b><i>geberekoo Bot</i></b></a>. 
Send me a photo of a plant and I will provide you with analysis of the plant.

Use <b>/help</b> to display this message.
"""
    await update.message.reply_text(help_message, parse_mode=ParseMode.HTML)


async def download_image_using_getfile(update, context):
    # Get file information
    file_id = update.message.photo[-1].file_id
    url = f"https://api.telegram.org/bot{TOKEN}/getFile"
    params = {"file_id": file_id}

    # ask telegrame for the image info
    response = requests.get(url, params=params)
    file_info = response.json()

    # Construct the download URL
    file_path = file_info["result"]["file_path"]
    download_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    # Download the file
    img_data = requests.get(download_url).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)

    # print("Image downloaded successfully!")

    # Send the image to the API endpoint
    api_url = "https://api-geberekoo.onrender.com/predict"
    files = {'file': ('image_name.jpg', img_data, 'image/jpeg')}
    response = requests.post(api_url, files=files)
    api_response = response.json()

    api_response = json.loads(api_response)


    response_text = f'''Plant Name: {api_response["plant_name"]}
    Common Name: {api_response["common_name"]}
    Genus: {api_response["genus"]}
    Scientific Name: {api_response["scientific_name"]}
    Status: {api_response["status"]}
    Disease: {api_response["disease"]}
    Description: {api_response["description"]}
    Causes: 
    \t- {"- ".join(api_response["causes"])}
    Symptoms:
    \t- {"- ".join(api_response["symptoms"])}
    Prevention or Treatment Mechanisms:
    \t- {"- ".join(api_response["prevention_or_treatment_mechanisms"])}
    Agrochemicals:
    \t- {"- ".join(api_response["agrochemicals"])}
    Pesticides:
    \t- {"- ".join(api_response["pesticides"])}
    Temperature: {api_response["temperature"]}
    Humidity: {api_response["humidity"]}'''

    # Sending the modified API response back to the user
    await update.message.reply_text(response_text)


if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), download_image_using_getfile))

    application.run_polling()
