# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23263522"))
API_HASH = getenv("API_HASH", "41aa1eab83b88e7af40346744ebdac07")
BOT_TOKEN = getenv("BOT_TOKEN", "7477343922:AAEdTAlWV7M-vuT0BlMVGUUfwKFRIaXD9Fk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5430826792").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://tweenex12:vYkha0VKY9XMQR3w@cluster0.2drdyk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1727909739")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1652946842"))
