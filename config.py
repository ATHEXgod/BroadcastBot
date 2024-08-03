import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6948767194:AAGE5qDxJOII1PEsZMa2iC8fB4UzMTPW6Yc")
API_ID = int(os.environ.get("API_ID", "28871407"))
API_HASH = os.environ.get("API_HASH", "d22f32d4606020695cb51cf9aa480ce9")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://rajeshpro123321:Vs9n8R90yUtCIyu4@clonestore1.w51yrrp.mongodb.net/?retryWrites=true&w=majority&appName=clonestore1")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
