from flask import Flask, request
import telegram

TOKEN = "8324131113:AAFQbIs_LAIe08c1xMFP75q1eFltASLHvNA"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"You said: {text}")
    return "OK"
