import dotenv, os


dotenv.load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
LOGIN_URL = os.environ.get('LOGIN_URL')