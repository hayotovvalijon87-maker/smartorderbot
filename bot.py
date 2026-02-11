import telebot

TOKEN = " 8086292265:AAHN06WpDGgKxtyQK-zCpD9S59hipgVEyWU "

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Салом 👋 Хуш омадед ба Smart Order Bot!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Паёми шумо қабул шуд ✅")

bot.polling()
