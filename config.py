# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBS_g7NiAKXRt-4oEHut9hepzRZ0J1SFVHi8zR87HWKWPm_42bO_iBLrsDHSDs2n1f9VpXnKkoyHj-YYF7I0Ur0F5Ou11LukpKnyfLqL8F3bhre7JY5IkfXYmhuQB3U29Rk15yamVFwPG1iuox6VRqOfn8d1SBO3EPHwdAAGZED9mmEZ7GLJ3MJagY4gHSAClGJSXzamkE7Xt1XH3GB8R1CL6GJYLAN2TZSXDHS PdAN19TP7hrzQ2tnJQip5ZZUgZeJiNvAVykDfMgESaPLM2Jk1JQBTmB4rQ0lSZfTTRlM19t93C5pzFogVRNPyZwsUB7br-kmTAAAAAXVD9GWA")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26331872"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c93589620441707c37c5683a02eea54e")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8413546109"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1003161993313")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ajmerasaini01:U1sGiZRI6Ha0xuCy@cluster0.tnok3d0.mongodb.net/") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
