from flask import Flask, request
import telebot
import os

TOKEN = "8324131113:AAFQbIs_LAIe08c1..."
bot = telebot.TeleBot(TOKEN)

WEBHOOK_URL = f"https://telegram-bot-qgf5.onrender.com/{TOKEN}"
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

app = Flask(__name__)

# Odpoveď na /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "✅ Hello!")

# Webhook handler
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# Úvodná stránka
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
