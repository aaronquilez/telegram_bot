import logging
import os
from dotenv improt load_dotenv
from datetime import date
import time

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv(os.path.join('.env'))
            
BOT_TOKEN = os.environ.get('BOT_TOKEN')
LOGIN_URL = os.environ.get('LOGIN_URL')

user_credentials = {}



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def login_and_download(login_url, username, password):

    driver = webdriver.Chrome()
    driver.get(login_url)

    driver.find_element(By.ID, 'data.email').send_keys(username)
    driver.find_element(By.ID, 'data.password').send_keys(password)

    driver.find_element(By.CLASS_NAME, 'fi-btn').click()

    return driver
   


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome!')


async def sendme(update, context: ContextTypes.DEFAULT_TYPE) -> None:

    saved_credentials = user_credentials.get(update.effective_chat.id)
    if saved_credentials:
        username = saved_credentials['username']
        password = saved_credentials['password']
 
        response = login_to_webpage(username, password)
        await update.message.reply_text(response)
    
    await update.message.reply_text("Usuari no registrat")


# Function to handle messages
async def handle_message(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user_input = update.message.text
    
    try:
        username, password = user_input.split(':')
        user_credentials[update.effective_chat.id] = {'username': username, 'password': password}
        response = login_to_webpage(username, password)
        await update.message.reply_text(response)
    except ValueError:
        await update.message.reply_text('Please provide credentials in the correct format.')

# Function to log in to the webpage
def login_to_webpage(username: str, password: str) -> str:
    

    today = date.today().strftime("%d-%m-%Y") 

    driver = login_and_download(LOGIN_URL, username, password)

    time.sleep(5)
    try: 
        elements = driver.find_elements(By.CLASS_NAME, 'ring-primary-600')
        dies = {}
        detall = []

        for e in elements:
            detall = e.text.splitlines()
            key = detall.pop(0)
            dies[key] = detall

        driver.quit()
        return (dies[today])
    except:
        return ("No s'ha registrat correctament")




# Main function to run the bot
def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sendme", sendme))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
