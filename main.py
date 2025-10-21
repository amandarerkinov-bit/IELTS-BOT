import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("7952799058:AAE3k0Vj-1cSJ_eot_tZ46b1I-HqRkKr7MI") or "7952799058:AAE3k0Vj-1cSJ_eot_tZ46b1I-HqRkKr7MI"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Salom! IELTS tayyorlov botiga xush kelibsiz.\n\nBuyruqlar:\n📘 /vocabulary – So‘z boyligini oshirish\n🗣 /speaking – Speaking mashqlari\n🧠 /tips – IELTS maslahatlar")

@bot.message_handler(commands=['vocabulary'])
def vocab(message):
    bot.reply_to(message, "Bugungi so‘z: *Accurate* – aniq, to‘g‘ri.\nMisol: Your answer is accurate ✅", parse_mode='Markdown')

@bot.message_handler(commands=['speaking'])
def speaking(message):
    bot.reply_to(message, "Speaking savol: What is your favorite book and why? 📚")

@bot.message_handler(commands=['tips'])
def tips(message):
    bot.reply_to(message, "Maslahat: Har kuni 5 ta yangi so‘z yodla va ularni gapda ishlat.")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://YOUR_RAILWAY_URL/' + TOKEN)
    return "Bot ishga tushdi!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)