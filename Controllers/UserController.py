from telegram import Update
from telegram.ext import ContextTypes
from datetime import date, timedelta


from Helpers.Login import *
from Models.User import *


user_credentials = {}


class UserController:

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Benvingut! Introdueix l\'usuari i contrasenya')


    async def sendme(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Sendme")
        day = date.today().strftime("%d-%m-%Y") 

        user = User.get_user_by_telegram_id(update.effective_chat.id)
        
        if user:   
            response = Login.login_to_webpage(user[1], user[2], day)
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Usuari no registrat")
            

    async def yesterday(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Yesteday")
        day = (date.today() - timedelta(days = 1)).strftime("%d-%m-%Y") 
        user = User.get_user_by_telegram_id(update.effective_chat.id)
        
        if user:   
            response = Login.login_to_webpage(user[1], user[2], day)
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Usuari no registrat")

   
    async def handle_message(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        
        day = date.today().strftime("%d-%m-%Y") 
        user_input = update.message.text
        
        try:
            username, password = user_input.split(':')
            user_credentials[update.effective_chat.id] = {'username': username, 'password': password}
            
            if not User.get_user_by_telegram_id(update.effective_chat.id):
                User.create_user(username, password, update.effective_chat.id)

            response = Login.login_to_webpage(username, password, day)
            await update.message.reply_text(response)
        except ValueError:
            await update.message.reply_text('Please provide credentials in the correct format.')



