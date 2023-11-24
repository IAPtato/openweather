from flask import Flask, render_template
import requests 
from dotenv import load_dotenv,dotenv_values

config = dotenv_values('.env')
    
app = Flask(__name__)

def get_weather_data(city):
    API_KEY= config['API_KEY']
    #url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=esp&units=metric'
    r = requests.get(url).json()
    #print(r)
    return r
ciudades=[]

@app.route('/prueba')
def prueba():
    clima= get_weather_data('city')
    temperatura = str(clima['main']['temp'])
    descripcion = str(clima['weather'] [0] ['description'])
    icono = str(clima['weather'] [0]['icon'])
    ciudad = str(clima['name'])
    pais= str(clima['sys']['country'])
    r_json={
        'ciudad': ciudad,
        'pais': pais,
        'temperatura': temperatura,
        'descripcion':descripcion,
        'icono':icono
    }
    return render_template('weather1.html',rj=r_json)

@app.route('/rjson')
def rjson():
    rjson= get_weather_data('quito')
    temperatura = str(rjson['main']['temp'])
    descripcion = str(rjson['weather'] [0] ['description'])
    icono = str(rjson['weather'] [0]['icon'])
    ciudad = str(rjson['name'])
    pais= str(rjson['sys']['country'])
   
    return (rjson)



@app.route('/weather')
def weather():
    return render_template('weather1.html')


@app.route('/cv')
def cv():
    return render_template('cv1.html')

@app.route('/cv1')
def cv1():
    return render_template('cv.html')

@app.route('/satur')
def satur():
    return render_template('satur.html')

if __name__ == '__main__':
    app.run(debug=True)
