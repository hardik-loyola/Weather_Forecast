import tkinter as tk
import requests

# Function to get weather data
def get_weather(lat, lon):
    api_key = 'b5508b18408a1951c9d1e43696eab784'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data:
        location = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Location: {location}\nWeather: {weather}\nTemperature: {temp}°C"
    else:
        return "Unable to fetch weather data."

# Function to get the user's current location using an IP geolocation API
def get_current_location():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    if data['status'] == 'success':
        weather_info = get_weather(data['lat'], data['lon'])
        result_label.config(text=weather_info)
    else:
        result_label.config(text="Unable to get location.")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x200")

# Label to display the weather information
result_label = tk.Label(root, text="Fetching weather...", font=("Helvetica", 14))
result_label.pack(pady=20)

# Automatically get weather data when the app starts
get_current_location()

# Start the Tkinter event loop
root.mainloop()
