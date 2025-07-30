import os
import telebot
from flask import Flask, request

API_TOKEN = '8324131113:AAFQbIs_LAIe08c1xMFP75q1eFltASLHvNA'  # ← tvoj token
bot = telebot.TeleBot(API_TOkdKEN)
app = Flask(__name__)

# /start príkaz
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your Bot.")

# Webhook route
@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

# Domovská stránka
@app.route("/", methods=['GET'])
def index():
    return "Bot is running!", 200

# Spustenie Flask servera
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
