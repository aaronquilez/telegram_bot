
from Bot import *  
from Controllers.UserController import UserController

from telegram.ext import CommandHandler, MessageHandler, filters 



# Main function to run the bot
def main() -> None:
    
    bressol_kp_bot = Bot()
    
    bressol_kp_bot.application.add_handlers([
        CommandHandler("start", UserController.start),
        CommandHandler("sendme", UserController.sendme),
        MessageHandler(filters.TEXT & ~filters.COMMAND, UserController.handle_message),
    ])

    bressol_kp_bot.run()


if __name__ == '__main__':
    main()
