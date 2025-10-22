import telebot
from flask import Flask, request
import os

# 🔹 Token
TOKEN = os.getenv("7952799058:AAE3k0Vj-1cSJ_eot_tZ46b1I-HqRkKr7MI")  # Railway environment variable
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 🔹 /start buyrug‘i
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Bot ishlayapti! Sizning bot 24/7 onlayn bo‘ladi 😎")

# 🔹 Webhook
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "OK", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_RAILWAY_URL/' + TOKEN)
    return "Bot ishga tushdi!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)