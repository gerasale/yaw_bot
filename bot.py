import config 
import telebot 
import weather_data
import write_log
from telebot import types

bot = telebot.TeleBot(config.token)

# markup = types.ReplyKeyboardMarkup()
# markup.row('Погода в Москве')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Напишите название города, чтобы получить текущую погоду')

@bot.message_handler(content_types=['text'])
def mes(message):
	bot.send_message(message.chat.id, weather_data.write_weather(message.text))
	write_log.write_log(message.text)



if __name__ == '__main__':
     bot.polling(none_stop=True)