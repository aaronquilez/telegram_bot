import logging
from telegram import Update
from telegram.ext import Application


from Constants.Env import BOT_TOKEN

class Bot:

    application: Application
    logger: logging.Logger

    def __init__(self):
        self.set_logger()
        self.application = Application.builder().token(BOT_TOKEN).build()


    def set_logger(self):
        logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
