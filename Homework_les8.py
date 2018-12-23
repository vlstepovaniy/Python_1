import json
import requests
import sqlite3




apfile = open('ap.id.txt', 'r', encoding='utf-8')
appid = apfile.read()

data_town = open('city.list.json', 'r', encoding='utf-8')
datatown = json.load(data_town)

def weather_town(city):   #Блок OpenWeatherMap
    
    ID = 0  #переменная id

    for town in datatown:
	    if town["name"] == city:
		    ID = (town["id"])

	
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'.format(ID, appid) 

    res = requests.get(url)

    data = res.json()

    temp = round(data['main']['temp'] - 273)
    wind_speed = data['wind']['speed']

    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    description = data['weather'][0]['description']

    print('Temperature : {} C'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))


city = input('Enter yor city : ')
weather_town(city)


# БД
# К сожалению, не смог реализовать блок работы с бд
# Если, это критично для сдачи дз, прошу продлить срок сдачи

