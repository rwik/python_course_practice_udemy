import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
obs = owm.weather_at_place('Bangalore')
weather = obs.get_weather()
temperature = weather.get_temperature(unit='celsius')['temp']

print('The temperature is ' + str(temperature) + ' degrees Fahrenheit.')
