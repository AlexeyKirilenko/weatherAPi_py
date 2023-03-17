import requests
from tkinter import *

# Create a function to get weather data from OpenWeatherMap API
def get_weather(city):
    api_key = 'API HERE' # Replace with your own API key
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


# Define colors
bg_color = '#222'
fg_color = '#fff'
btn_bg_color = '#00bcd4'
btn_fg_color = '#fff'

# Configure root widget
root.config(bg=bg_color)

# Create a frame for the content
content_frame = Frame(root, bg=bg_color, padx=20, pady=20)
content_frame.pack()

# Create widgets
city_label = Label(content_frame, text='Enter city name:', fg=fg_color, font=('Helvetica', 16), pady=10)
city_label.pack()

city_entry = Entry(content_frame, font=('Helvetica', 14), width=25)
city_entry.pack()

submit_button = Button(content_frame, text='Get Weather', command=show_weather, bg=btn_bg_color, fg=btn_fg_color, font=('Helvetica', 14), padx=10, pady=5)
submit_button.pack(pady=10)

weather_label = Label(content_frame, text='', fg=fg_color, font=('Helvetica', 14), pady=10)
weather_label.pack()

# Apply styles using CSS
style = """
.TLabel {
    background-color: #222;
    color: #fff;
    font-size: 14px;
    font-weight: normal;
}
.TEntry {
    background-color: #333;
    color: #fff;
    font-size: 14px;
    font-weight: normal;
    border: none;
    padding: 5px;
}
.TButton {
    background-color: #00bcd4;
    color: #fff;
    font-size: 14px;
    font-weight: bold;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
}
.TButton:hover {
    background-color: #008c9e;
}
"""

root.tk.eval('''
    package require ttk
    ttk::style awdarkstyle {'''+style+'''}
    ttk::style awdarkstyle.Treeview {{}}
    ttk::style awdarkstyle.TLabel {style awdarkstyle.TLabel}
    ttk::style awdarkstyle.TEntry {style awdarkstyle.TEntry}
    ttk::style awdarkstyle.TButton {style awdarkstyle.TButton}
''')

city_label.configure(style='awdarkstyle.TLabel')
city_entry.configure(style='awdarkstyle.TEntry')
submit_button.configure(style='awdarkstyle.TButton')
weather_label.configure(style='awdarkstyle.TLabel')

root.mainloop()
