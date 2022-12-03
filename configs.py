import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "15823382"))
    API_HASH = os.getenv("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5918078029:AAFN-9kReJNA1-S4mn3JyLljr6orP9HnGCM")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "BQBUiK8_23AiLBM7skYoQe9reYcvUXjGvYYHB7II8PU0R52nQ2jPmjmKLFl-_hKDa0Ojb3oJdedCbj_wu2ej7zk-midZ8xR7cz8AFfeZZ2D1sY1AAskkrPqsGCXhGJKd3T_x0kKMYO3J1LRXr8pubTo1jdGRFAaiO_nMWRy8Wh_Xiy-lg5OYl6Rs8ZYIOMNA-xSEVU8p_dZRrR9W_tfUwUUNw_yO1beLiAKHfpAMMyDxEKuqGt3xLhhKo4-cOqF7NL11zLKxoYVblMIKx-TCNCUUNKteGPOZ_mFJa4Ihwp_U2S3i-u3d0ioEyHx4gBDkVg8z0QRwW1FgPXTNVahldS8pAAAAATA9VkIA>
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001767857004"))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "Mdisk_search_re_bot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "5104293442"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "tlgbotsowner")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "daagffgd")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", "Wait" )
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/b57323ed245c34a374ac4.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", "Wait" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "daagffgd")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://W9Uyj61afEXSw601:W9Uyj61afEXSw601@cluster0.zsxso.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001529577466"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "daagffgd")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "UM1dBYJxSu9QO1S9s8Tv")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", "Jald")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", "Soon" )
