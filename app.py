from flask import Flask, request, render_template
import requests, time

app = Flask(__name__)

@app.route('/city')
@app.route('/')
def city():
    return render_template('city.html')

@app.route('/weather', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST' and request.form.get('area') != '':
        city = request.form.get('area')

        # weatherStart
        api_key = '883bd1f2a3ee381200a54108db3f5ecd'
        link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(link)
        data = response.json()

        if data['cod'] == 200:
            link_img = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
            return render_template('weather.html', country=data['sys']['country'], city=data['name'],
                                   weather=data['weather'][0]['main'],
                                   desc=data['weather'][0]['description'].capitalize(),
                                   temp=(format(data['main']['temp'] - 273.15, '.2f')),
                                   updated=time.ctime(int(data['dt'])),
                                   img = link_img
                                   )
        else:
            return render_template('city.html')
    else:
        return render_template('city.html')

if __name__ == '__main__':
    app.run()
