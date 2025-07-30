from flask import Flask, request
import telebot

TOKEN = "8324131113:AAFQbIs_LAIe08c1xMFP75q1eFltASLHvNA"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Odpoveď na /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "✅ Hello! Bot is working.")

# Webhook handler
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    bot.process_new_updates([update])
    return "OK", 200

# Úvodná stránka
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200

if __name__ == '__main__':
    app.run(debug=True)
