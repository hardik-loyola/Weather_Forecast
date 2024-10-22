import tkinter as tk
import requests

# Function to convert a color name to an (R, G, B) tuple
def name_to_rgb(color_name):
    r, g, b = root.winfo_rgb(color_name)  # Convert color name to RGB values using Tkinter's winfo_rgb
    return r // 256, g // 256, b // 256  # Scale the values from 0-65535 to 0-255

# Function to convert an (R, G, B) tuple to hex color string
def rgb_to_hex(rgb_color):
    return f'#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}'

def calculate_brightness(rgb_color):
    return 0.299 * rgb_color[0] + 0.587 * rgb_color[1] + 0.114 * rgb_color[2]

# Function to get the appropriate text color based on background brightness
def get_text_color(rgb_color):
    brightness = calculate_brightness(rgb_color)
    return 'black' if brightness > 128 else 'white'

# Function to gradually change the background color and adjust text color
def smooth_transition(start_rgb, end_rgb, steps=30, delay=30):
    if start_rgb == end_rgb:
        return

    def step_color_change(step):
        if step > steps:
            return  # End the transition

        # Interpolate the RGB values
        current_rgb = [
            int(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * step / steps)
            for i in range(3)
        ]
        # Convert the RGB back to hex format and update backgrounds
        current_color = rgb_to_hex(current_rgb)
        text_color = get_text_color(current_rgb)  # Get appropriate text color based on brightness

        # Update background and text colors
        root.config(bg=current_color)
        for label in weather_labels:
            label.config(bg=current_color, fg=text_color)

        # Schedule next color change
        root.after(delay, step_color_change, step + 1)

    # Start the color transition
    step_color_change(0)

# Function to get weather data by location name (city)
def get_weather_by_city(city):
    api_key = 'b5508b18408a1951c9d1e43696eab784'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data and data.get('cod') == 200:
        location = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Determine color based on weather condition
        weather_colors = {
            "clear sky": "lightyellow",
            "few clouds": "lightgray",
            "scattered clouds": "lightblue",
            "rain": "lightgreen",
            "snow": "snow",
            "thunderstorm": "lightcoral"
        }
        weather_condition = data['weather'][0]['main'].lower()
        color_name = weather_colors.get(weather_condition, "lightblue")  # Default to lightblue if condition not mapped

        return {
            'location': location,
            'weather': weather.capitalize(),
            'temp': f"{temp}°C",
            'humidity': f"{humidity}%",
            'wind': f"{wind_speed} m/s",
            'color': color_name
        }
    else:
        return None

# Function to get weather data for user's current location
def get_weather_by_coordinates(lat, lon):
    api_key = 'b5508b18408a1951c9d1e43696eab784'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data:
        location = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Determine color based on weather condition
        weather_colors = {
            "clear sky": "lightyellow",
            "few clouds": "lightgray",
            "scattered clouds": "lightblue",
            "rain": "lightgreen",
            "snow": "snow",
            "thunderstorm": "lightcoral"
        }
        weather_condition = data['weather'][0]['main'].lower()
        color_name = weather_colors.get(weather_condition, "lightblue")  # Default to lightblue if condition not mapped

        return {
            'location': location,
            'weather': weather.capitalize(),
            'temp': f"{temp}°C",
            'humidity': f"{humidity}%",
            'wind': f"{wind_speed} m/s",
            'color': color_name
        }
    else:
        return None

# Function to get the user's current location using an IP geolocation API
def get_current_location():
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    if data['status'] == 'success':
        weather_data = get_weather_by_coordinates(data['lat'], data['lon'])
        if weather_data:
            update_weather_display(weather_data)
        else:
            location_label.config(text="Unable to fetch weather data for current location.")
    else:
        location_label.config(text="Unable to get current location.")

# Function to search and update weather based on user input
def search_weather():
    city = search_entry.get()  # Get the input from the search bar
    if city:
        weather_data = get_weather_by_city(city)
        if weather_data:
            update_weather_display(weather_data)
        else:
            location_label.config(text="City not found. Please try again.")
    else:
        location_label.config(text="Please enter a city name.")

# Function to update the weather display
def update_weather_display(weather_data):
    location_label.config(text=f"Location: {weather_data['location']}")
    temp_label.config(text=f"Temperature: {weather_data['temp']}")
    weather_label.config(text=f"Weather: {weather_data['weather']}")
    humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
    wind_label.config(text=f"Wind: {weather_data['wind']}")

    # Start color transition
    current_color = root.cget('bg')
    start_rgb = name_to_rgb(current_color)
    end_rgb = name_to_rgb(weather_data['color'])
    smooth_transition(start_rgb, end_rgb)

# Tkinter GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg='white')

# Search bar and button
search_entry = tk.Entry(root, font=("Helvetica", 14), width=20)
search_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", font=("Helvetica", 14), command=search_weather)
search_button.pack(pady=5)

# Weather Info Labels
location_label = tk.Label(root, text="Location:", font=("Helvetica", 14), bg='white')
temp_label = tk.Label(root, text="Temperature:", font=("Helvetica", 14), bg='white')
weather_label = tk.Label(root, text="Weather:", font=("Helvetica", 14), bg='white')
humidity_label = tk.Label(root, text="Humidity:", font=("Helvetica", 14), bg='white')
wind_label = tk.Label(root, text="Wind:", font=("Helvetica", 14), bg='white')

# List of labels for easier color management
weather_labels = [location_label, temp_label, weather_label, humidity_label, wind_label]

# Layout for the labels
location_label.pack(pady=5)
temp_label.pack(pady=5)
weather_label.pack(pady=5)
humidity_label.pack(pady=5)
wind_label.pack(pady=5)

# Fetch weather for the user's current location when the app starts
get_current_location()

# Start the Tkinter event loop
root.mainloop()
