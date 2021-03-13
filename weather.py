import pyowm

owm=pyowm.OWM('60ba9c53fab7777517cb2eff0909d1f0')

city='New Delhi'
loc=owm.Weather_at_place(city)
weather=loc.get_weather()

temp=weather.get_temperature(unit='celsius')

for Key, val in temp.item():
    print(f'{key} = {val}')

humidity=weather.get_humidity()
wind=weather.get_wind()
rain=weather.get_rain()

print(f'humidity={humidity}')
print(f'wind={wind}')
print(f'rain={rain}')

sr=weather.get_sunrise_time(timeformat='iso')
ss=weather.get_sunset_time(timeformat='iso')
print(f'SunRise={sr}')
print(f'SunSet={ss}')


clouds=str(loc.will_have_clouds())
rain=str(loc.will_have_rain())

print('Will have clouds'+ clouds)
print('Will have rain'+ rain)