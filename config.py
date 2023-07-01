import os


class Config(object):
    API_HASH = os.environ.get("cf2a75861140ceb746c7796e07cbde9e")
    BOT_TOKEN = os.environ.get("5613307332:AAEVpbfhPpEMQYd2g1f9FjHC53FnTDVw8WI")
    TELEGRAM_API = os.environ["27353035"]
    OWNER = os.environ.get("1327021082")
    OWNER_USERNAME = os.environ.get("RGAnimeLover")
    PASSWORD = os.environ.get("ruhan9366")
    DATABASE_URL = os.environ.get("mongodb+srv://rgisop:ruhan9366@cluster0.rx5ptxg.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001914381778")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("BQClr4aJRb4iX4bYEpRfD3fZsyR1WugvjjDQG5ArM0uSzglGT68_Huuq-9wVNf0buGBTb8K9anhqRCwFCpvejZlLV9JVBv-Oz-wpzK7R_bRxiOMNaaFSNFYkA-AF8lpFG40FMhbrKJLTEAp74vs39F0PjJPOPp0iXiq3sMA9pVXQHG0eZprHetrkjrFcMj7C3upBC0KXHB_A3WUn9pam1tpnx1okudCIby593ld2h5b57qrFN7EsHM6eMbdP2zvNjY80Kbsdq7-3i1su9EsB6_iKO-o6s363ZlsbYJRke4T_RxwK1RUoVkQsXFPMYNXB2LtAuXAM5DYb5eV7mY5VyvlFAAAAAUQDTKsA", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
