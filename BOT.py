import telebot
from telebot import types

api = "6516440387:AAEdVNGtNqYjSP6ACf_FWkeox98fM-O_jxc"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Кнопка")
  markup.add(item1)																																					
  bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
bot.infinity_polling()
