from flask import Flask, request
import telegram
import logging
import os

TOKEN = os.environ.get("TOKEN") or "sem_daj_token_ak_nemas_env"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# Nastav logovanie do konzoly
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

@app.route(f"/{TOKEN}/", methods=["POST"])
def respond():
    logging.info("DOSTAL som požiadavku z Telegramu.")
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    
    chat_id = update.message.chat.id
    message_text = update.message.text
    logging.info(f"Správa od {chat_id}: {message_text}")

    if message_text == "/start":
        bot.sendMessage(chat_id=chat_id, text="Ahoj! Som živý a odpovedám!")
    else:
        bot.sendMessage(chat_id=chat_id, text="Napíš /start pre privítanie.")

    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Bot je online a pripravený."

if __name__ == "__main__":
    app.run(port=5000)
