import pyowm
import time
def write_weather(count):
	if count>1:
		city = 'Москва'
		owm = pyowm.OWM('2f4a0bf366b1d30befe718267483b66c', language='ru')
		obs = owm.weather_at_place(city)
		w = obs.get_weather()
		data = [('Сейчас в городе ' + city + ': ' + w.get_detailed_status()), ('Видимость: ' + str(w.get_humidity()) + '%'), ('Температура сейчас: ' + str(w.get_temperature(unit='celsius')['temp']) + ' градусов цельсия'), ('Максимальная температура сегодня: ' +
	                                                                                                                                                                                                                     str(w.get_temperature(unit='celsius')['temp_max']) + ' градусов цельсия'), ('Минимальная температура сегодня: ' + str(w.get_temperature(unit='celsius')['temp_min']) + ' градусов цельсия'), ('Скорость ветра: ' + str(w.get_wind()['speed']) + ' м/с'), ('Текущее время: ' + time.asctime())]
		return data[0] + '\n' + data[1]+ '\n' + data[2]+ '\n' + data[3]+ '\n' + data[4]+ '\n' + data[5] + '\n' +data[6]