import requests,json
city = 'erode'
api_key = '883bd1f2a3ee381200a54108db3f5ecd'
link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(link)
data = response.json()
if data['cod'] != 401:
    print('Country: ',data['sys']['country'])
    print('City: ',data['name'])
    print('Lattitude: ',data['coord']['lat'])
    print('Longitude: ', data['coord']['lon'])
    print('Weather: ',data['weather'][0]['main'])
    print('Description: ',data['weather'][0]['description'].capitalize())
    print('Temperature: ',format(data['main']['temp']-273.15,'.2f') )