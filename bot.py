import os
import requests
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

USERNAME_INDO = os.environ.get("USERNAME_INDO")
PASSWORD_INDO = os.environ.get("PASSWORD_INDO")

app = Client("indopaket_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def login_indopaket():
    session = requests.Session()
    login_url = "https://indopaket.com/login"
    data = {
        "username": USERNAME_INDO,
        "password": PASSWORD_INDO
    }
    res = session.post(login_url, data=data)
    if res.status_code == 200:
        return session
    return None

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Bot aktif ✅\nKirim /titip untuk proses paket.")

@app.on_message(filters.command("titip"))
def titip(client, message):
    session = login_indopaket()
    if session:
        message.reply_text("Login berhasil ✅\nProses titip paket dijalankan.")
    else:
        message.reply_text("Login gagal ❌")

app.run()
