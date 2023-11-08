import telebot
from telebot import types

api = "6516440387:AAEdVNGtNqYjSP6ACf_FWkeox98fM-O_jxc"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет это PILG-бот, ты можешь узнать обо мне с помощью комманды /podrobnee , для помощи используй /help, а так же можешь обратиться в поддержку - /podderjka')
	
@bot.message_handler(commands=['podderjka'])
def start_message(message):
    bot.send_message(message.6261355188, f'send - {message.text}')
	bot.send_message(message.chat.id, f'поддержке отправленно сообщение - {message.text}')

@bot.message_handler(commands=['podrobnee'])
def start_message(message):
	bot.send_message(message.chat.id,'text o bote')

@bot.message_handler(commands=['help'])
def start_message(message):
	bot.send_message(message.chat.id,'help')


bot.infinity_polling()
