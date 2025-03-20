import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '29525287'))
API_HASH = environ.get('API_HASH', 'f9e7627252d42bea8a120e80bacd11d6')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Start message pictures
PICS = environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg').split()

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7663483746').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Log channel
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002374499720'))

# File Channel
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002457797957').split()]

# Force subscribe channel
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-4608019635')) if environ.get('AUTH_CHANNEL', '').isdigit() else None

# Request channel
REQST_CHANNEL = int(environ.get('REQST_CHANNEL', '')) if environ.get('REQST_CHANNEL', '').isdigit() else None

# Support chat
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '-4647428616')) if environ.get('SUPPORT_CHAT_ID', '').isdigit() else None

# File storage
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split() if ch.isdigit()]
DELETE_CHANNELS = [int(dch) for dch in environ.get('DELETE_CHANNELS', '4667478009').split() if dch.isdigit()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://tboxmove:HkhLBoLvv03Ozvht@cluster0.5yuuw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjclonefilterbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')

# Boolean settings
MULTIPLE_DATABASE = environ.get('MULTIPLE_DATABASE', 'False').lower() == 'true'
PREMIUM_AND_REFERAL_MODE = environ.get('PREMIUM_AND_REFERAL_MODE', 'True').lower() == 'true'
STREAM_MODE = environ.get('STREAM_MODE', 'True').lower() == 'true'
AUTO_APPROVE_MODE = environ.get('AUTO_APPROVE_MODE', 'False').lower() == 'true'
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', 'False').lower() == 'true'

# Payment settings
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 30ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜ\n- 120ʀs - 3 ᴍᴏɴᴛʜs\n- 220ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁</b>')

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+d64NJgw7W6AxN2Jk')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/vj_botz')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/kingvj01')

# Shortlink settings
SHORTLINK_MODE = environ.get('SHORTLINK_MODE', 'False').lower() == 'true'
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

# Cache settings
CACHE_TIME = int(environ.get('CACHE_TIME', '1800'))
PORT = int(environ.get("PORT", "8080"))

# Feature toggles
AI_SPELL_CHECK = environ.get('AI_SPELL_CHECK', 'True').lower() == 'true'
PM_SEARCH = environ.get('PM_SEARCH', 'True').lower() == 'true'
BUTTON_MODE = environ.get('BUTTON_MODE', 'True').lower() == 'true'
AUTO_DELETE = environ.get('AUTO_DELETE', 'True').lower() == 'true'

# Reaction emojis for start command
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# Choose Option Settings
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]
EPISODES = [f"E{str(i).zfill(2)}" for i in range(1, 41)]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = [str(i) for i in range(1900, 2026)]

# Handle multiple database mode
if not MULTIPLE_DATABASE:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = environ.get('O_DB_URI', DATABASE_URI)  
    OTHER_DB_URI = environ.get('O_DB_URI', "")  
    FILE_DB_URI = environ.get('F_DB_URI', "")  
    SEC_FILE_DB_URI = environ.get('S_DB_URI', "")  

# Ensure required variables are set
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Missing required environment variables: API_ID, API_HASH, BOT_TOKEN.")

if AUTH_CHANNEL is None:
    print("Warning: AUTH_CHANNEL is not set properly!")

if SUPPORT_CHAT_ID is None:
    print("Warning: SUPPORT_CHAT_ID is not set properly!")

# Final confirmation that script is loaded
print("Bot configuration loaded successfully.")