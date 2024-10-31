from telegram import Update
from telegram.ext import ContextTypes
from datetime import date, timedelta


from Helpers.Login import *


user_credentials = {}


class UserController:

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Benvingut! Introdueix l\'usuari i contrasenya')


    async def sendme(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Sendme")
        day = date.today().strftime("%d-%m-%Y") 
        saved_credentials = user_credentials.get(update.effective_chat.id)
        if saved_credentials:
            username = saved_credentials['username']
            password = saved_credentials['password']
    
            response = Login.login_to_webpage(username, password, day)
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Usuari no registrat")

    async def yesterday(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Yesteday")
        day = (date.today() - timedelta(days = 1)).strftime("%d-%m-%Y") 
        saved_credentials = user_credentials.get(update.effective_chat.id)
        if saved_credentials:
            username = saved_credentials['username']
            password = saved_credentials['password']
    
            response = Login.login_to_webpage(username, password, day)
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Usuari no registrat")

   
    async def handle_message(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        day = date.today().strftime("%d-%m-%Y") 
        user_input = update.message.text
        
        try:
            username, password = user_input.split(':')
            user_credentials[update.effective_chat.id] = {'username': username, 'password': password}
            response = Login.login_to_webpage(username, password, day)
            await update.message.reply_text(response)
        except ValueError:
            await update.message.reply_text('Please provide credentials in the correct format.')



