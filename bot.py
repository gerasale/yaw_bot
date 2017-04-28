import config 
import telebot 
import weather_data
#from telebot import types

bot = telebot.TeleBot(config.token)

#markup = types.ReplyKeyboardMarkup()
#markup.row('Погода в Москве')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def message(message):
	bot.send_message(message.chat.id, weather_data.write_weather(2), reply_markup=markup)



if __name__ == '__main__':
	bot.polling(none_stop=True)
