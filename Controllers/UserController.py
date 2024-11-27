from telegram import Update
from telegram.ext import ContextTypes
from datetime import date, timedelta


from Helpers.Login import *
from Models.User import *
from Helpers.BeautifyResponse import *



class UserController:

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('Benvingut! Introdueix l\'usuari i contrasenya')


    async def sendme(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Sendme")
        print("Chat id: " + str(update.effective_chat.id))
        
        day = date.today().strftime("%d-%m-%Y") 
        user = User.get_user_by_telegram_id(update.effective_chat.id)     
        
        if user:   
            response = Login.login_to_webpage(user[1], user[2])
            result = BeautifyResponse.beautify(response, day)
            await update.message.reply_text(result)
        else:
            await update.message.reply_text("Usuari no registrat")
            

    async def yesterday(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Command send: Yesteday")
        print("Chat id: " + str(update.effective_chat.id))
        
        day = (date.today() - timedelta(days = 1)).strftime("%d-%m-%Y") 
        user = User.get_user_by_telegram_id(update.effective_chat.id)
        
        if user:   
            response = Login.login_to_webpage(user[1], user[2])
            result = BeautifyResponse.beautify(response, day)
            await update.message.reply_text(result)
        else:
            await update.message.reply_text("Usuari no registrat")

   
    async def handle_message(update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print("Message Received")
        day = date.today().strftime("%d-%m-%Y") 
        user_input = update.message.text
        
        try:
            username, password = user_input.split(':')

            print("Username: " + username)    
            if not User.get_user_by_telegram_id(update.effective_chat.id):
                User.create_user(username, password, update.effective_chat.id)
                print("User created")

            response = Login.login_to_webpage(username, password)
            result = BeautifyResponse.beautify(response, day)
            
            await update.message.reply_text(result)
        except ValueError:
            await update.message.reply_text('Please provide credentials in the correct format.')

    



