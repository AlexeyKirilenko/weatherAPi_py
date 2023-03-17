import requests
from tkinter import *

# Create a function to get weather data from OpenWeatherMap API
def get_weather(city):
    api_key = 'api key HERE' # Replace with your own API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Create a function to display weather data in the UI
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    weather_label.config(text=f'Temperature: {temperature}°C\nDescription: {description}')

# Create the UI
root = Tk()
root.title('Weather App')

city_label = Label(root, text='Enter city name:')
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

submit_button = Button(root, text='Get Weather', command=show_weather)
submit_button.pack()

weather_label = Label(root, text='')
weather_label.pack()

root.mainloop()
