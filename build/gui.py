# Import required libraries
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import requests
from datetime import datetime

# Set up path handling for assets/images
SCRIPT_DIR = Path(__file__).parent.absolute()
ASSETS_PATH = SCRIPT_DIR / "assets"

# Helper function to construct paths to asset files
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_weather_by_city(city):
    api_key = 'b5508b18408a1951c9d1e43696eab784'
    # Get forecast data including hourly forecast
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:

        current_response = requests.get(current_url)
        forecast_response = requests.get(forecast_url)

        current_data = current_response.json()
        forecast_data = forecast_response.json()

        if current_data and current_data.get('cod') == 200:
            # Current weather data
            location = current_data['name']
            weather_desc = current_data['weather'][0]['description']
            temp = current_data['main']['temp']
            temp_f = (temp * 9 / 5) + 32
            humidity = current_data['main']['humidity']
            wind_speed = current_data['wind']['speed']
            rain_chance = 0
            if forecast_data.get('list') and len(forecast_data['list']) > 0:
                rain_chance = forecast_data['list'][0].get('pop', 0) * 100
            # Convert sunset and sunrise times
            sunrise_time = datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%I:%M %p')
            sunset_time = datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%I:%M %p')

            def get_simplified_weather_description(weather_desc, is_day):
                # Create mapping of OpenWeatherMap descriptions to simplified categories
                weather_mapping = {
                    # Clear sky conditions
                    'clear sky': 'clear sky (sunny)' if is_day else 'clear sky (night)',

                    # Cloudy conditions
                    'broken clouds': 'cloudy',
                    'overcast clouds': 'cloudy',

                    # Partly cloudy conditions
                    'few clouds': 'partly cloudy (day)' if is_day else 'partly cloudy (night)',
                    'scattered clouds': 'partly cloudy (day)' if is_day else 'partly cloudy (night)',

                    # Rain conditions
                    'light rain': 'raining',
                    'moderate rain': 'raining',
                    'heavy intensity rain': 'raining',
                    'very heavy rain': 'raining',
                    'extreme rain': 'raining',
                    'freezing rain': 'raining',
                    'light intensity shower rain': 'raining',
                    'shower rain': 'raining',
                    'heavy intensity shower rain': 'raining',
                    'ragged shower rain': 'raining',
                    'light intensity drizzle': 'raining',
                    'drizzle': 'raining',
                    'heavy intensity drizzle': 'raining',
                    'shower rain and drizzle': 'raining',

                    # Thunder conditions
                    'thunderstorm': 'thunder',
                    'thunderstorm with light rain': 'thunder',
                    'thunderstorm with rain': 'thunder',
                    'thunderstorm with heavy rain': 'thunder',
                    'light thunderstorm': 'thunder',
                    'heavy thunderstorm': 'thunder',
                    'ragged thunderstorm': 'thunder',
                }

                return weather_mapping.get(weather_desc.lower(), weather_desc)

            daily_forecasts = []
            days_processed = set()
            current_date = datetime.now().date()

            for forecast in forecast_data['list']:
                forecast_date = datetime.fromtimestamp(forecast['dt']).date()
                day_name = forecast_date.strftime('%A')

                # Only process each day once and get the first forecast for each day
                if day_name not in days_processed and len(days_processed) < 7:
                    days_processed.add(day_name)

                    # Get weather condition for this day
                    weather_condition = forecast['weather'][0]['description']
                    is_day = True  # Assume daytime for forecasts
                    simplified_weather = get_simplified_weather_description(weather_condition, is_day)

                    daily_forecasts.append({
                        'day': day_name,
                        'weather': simplified_weather
                    })

            current_time = datetime.now().timestamp()
            is_day = current_data['sys']['sunrise'] < current_time < current_data['sys']['sunset']

            # Get the simplified weather description
            simplified_desc = get_simplified_weather_description(weather_desc, is_day)

            # Add windy condition if wind speed is high (you can adjust the threshold)
            if wind_speed > 8.0:  # if wind speed is greater than 8 m/s
                if simplified_desc in ['clear sky (sunny)', 'clear sky (night)']:
                    simplified_desc = 'windy'
                else:
                    simplified_desc = f"{simplified_desc}, windy"
            # Initialize hourly temps
            hourly_temps = {}

            # Process 5-day/3-hour forecast for hourly temperatures
            if forecast_data.get('list'):
                current_day = datetime.now().date()

                # Filter forecast entries for the current day
                today_forecasts = [
                    entry for entry in forecast_data['list']
                    if datetime.fromtimestamp(entry['dt']).date() == current_day
                ]

                # Map each forecast to the nearest time slot
                for forecast in today_forecasts:
                    forecast_time = datetime.fromtimestamp(forecast['dt'])
                    hour = forecast_time.hour
                    temp = (forecast['main']['temp'] * 9 / 5) + 32  # Convert to Fahrenheit

                    # Map hours to your specific time slots
                    if 22 <= hour or hour < 2:  # Around midnight
                        hourly_temps["12am"] = f"{round(temp)}°F"
                    elif 2 <= hour < 6:  # Around 4am
                        hourly_temps["4am"] = f"{round(temp)}°F"
                    elif 6 <= hour < 10:  # Around 8am
                        hourly_temps["8am"] = f"{round(temp)}°F"
                    elif 10 <= hour < 14:  # Around noon
                        hourly_temps["12pm"] = f"{round(temp)}°F"
                    elif 14 <= hour < 18:  # Around 4pm
                        hourly_temps["4pm"] = f"{round(temp)}°F"
                    elif 18 <= hour < 22:  # Around 8pm
                        hourly_temps["8pm"] = f"{round(temp)}°F"

            # Fill in any missing time slots with current temperature
            default_temp = f"{round(temp_f)}°F"
            for time_slot in ["12am", "4am", "8am", "12pm", "4pm", "8pm"]:
                if time_slot not in hourly_temps:
                    hourly_temps[time_slot] = default_temp

            return {
                'location': location,
                'temp': f"{round(temp_f)}°F",
                'humidity': f"{humidity}%",
                'wind_speed': f"{wind_speed} m/s",
                'sunrise': sunrise_time,
                'sunset': sunset_time,
                'hourly_forecast': hourly_temps,
                'weather_desc': simplified_desc,
                'rain_chance': f"{round(rain_chance)}%",
                'daily_forecasts': daily_forecasts
            }

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
# Function to handle time-based images (e.g., 12am, 4am) based on weather conditions

def search_weather():
    city = entry_1.get()  # Get the input from the search bar
    if city:
        weather_data = get_weather_by_city(city)
        if weather_data:

            # Update hourly forecast icons based on weather conditions
            hourly_forecasts = weather_data.get('hourly_forecast', {})
            current_time = datetime.now()
            sunrise_time = datetime.strptime(weather_data['sunrise'], '%I:%M %p').time()
            sunset_time = datetime.strptime(weather_data['sunset'], '%I:%M %p').time()

            for time_slot, temp in hourly_forecasts.items():
                # Convert time slot to datetime for day/night checking
                if time_slot == "12am":
                    hour = 0
                elif time_slot == "4am":
                    hour = 4
                elif time_slot == "8am":
                    hour = 8
                elif time_slot == "12pm":
                    hour = 12
                elif time_slot == "4pm":
                    hour = 16
                elif time_slot == "8pm":
                    hour = 20

                check_time = current_time.replace(hour=hour, minute=0)
                is_daytime = sunrise_time <= check_time.time() <= sunset_time

                # Determine which image to use based on weather description
                weather_desc = weather_data['weather_desc']
                image_path = None
                if weather_desc == 'clear sky (sunny)' and is_daytime:
                    image_path = "image_15.png"
                elif weather_desc == 'clear sky (night)' or (weather_desc == 'clear sky (sunny)' and not is_daytime):
                    image_path = "image_6.png"
                elif weather_desc == 'partly cloudy (day)' and is_daytime:
                    image_path = "image_8.png"
                elif weather_desc == 'partly cloudy (night)' or (
                        weather_desc == 'partly cloudy (day)' and not is_daytime):
                    image_path = "image_8.png"
                elif weather_desc == 'thunder':
                    image_path = "image_10.png"
                elif weather_desc == 'raining':
                    image_path = "image_5.png"
                elif weather_desc == 'windy':
                    image_path = "image_12.png"
                elif weather_desc == 'cloudy':
                    image_path = "image_2.png"
                else:
                    image_path = "image_2.png"  # Default to clear sky

                # Update the appropriate time slot's image
                if image_path:
                    new_image = PhotoImage(file=relative_to_assets(image_path))
                    if time_slot == "12am":
                        canvas.itemconfig(image_1, image=new_image)
                        canvas.midnight_image = new_image  # Keep reference
                    elif time_slot == "4am":
                        canvas.itemconfig(image_11, image=new_image)
                        canvas.early_morning_image = new_image
                    elif time_slot == "8am":
                        canvas.itemconfig(image_4, image=new_image)
                        canvas.morning_image = new_image
                    elif time_slot == "12pm":
                        canvas.itemconfig(image_9, image=new_image)
                        canvas.noon_image = new_image
                    elif time_slot == "4pm":
                        canvas.itemconfig(image_7, image=new_image)
                        canvas.afternoon_image = new_image
                    elif time_slot == "8pm":
                        canvas.itemconfig(image_6, image=new_image)
                        canvas.evening_image = new_image
            canvas.delete("location_text")  # Delete previous location text
            canvas.create_text(
                370.0,
                215.0,
                anchor="nw",
                text=weather_data['location'],
                fill="#221D1D",
                font=("Inter SemiBold", 20 * -1),
                tags="location_text")
            # Update the temperature text on the canvas
            canvas.delete("temperature_text")  # Delete previous temperature text
            canvas.create_text(
                265.0,
                220.0,
                anchor="nw",
                text=(weather_data['temp']),
                fill="#221D1D",
                font=("Inter", 140),
                tags="temperature_text")
            canvas.delete("humidity_txt")
            canvas.create_text(
                203.0,
                332.0,
                anchor="nw",
                text=(weather_data['humidity']),
                fill="#221D1D",
                font=("Inter SemiBold", 12 * -1),
                tags="humidity_txt")
            canvas.delete("wind_speed_txt")
            canvas.create_text(
                220.0,
                431.0,
                anchor="nw",
                text=(weather_data['wind_speed']),
                fill="#221D1D",
                font=("Inter SemiBold", 12 * -1),
                tags="wind_speed_txt")
            canvas.delete("rain_chance_txt")
            canvas.create_text(
                334.0,
                390.0,
                anchor="nw",
                text=f"Chances of rain: {weather_data['rain_chance']}",
                fill="#221D1D",
                font=("Inter SemiBold", 20 * -1),
                tags="rain_chance_txt")

            canvas.delete("sunrise_time")
            canvas.create_text(
                154.0,
                140.0,
                anchor="nw",
                text=(weather_data['sunrise']),
                fill="#221D1D",
                font=("Inter SemiBold", 12 * -1), tags="sunrise_time")

            canvas.delete("sunset_time")
            canvas.create_text(
                154.0,
                236.0,
                anchor="nw",
                text=(weather_data['sunset']),
                fill="#221D1D",
                font=("Inter SemiBold", 12 * -1), tags="sunset_time")


            for time_slot, temp in weather_data['hourly_forecast'].items():
                if time_slot == "12am":
                    canvas.delete("12am_temp")
                    canvas.create_text(
                        70.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="12am_temp")
                elif time_slot == "4am":
                    canvas.delete("4am_temp")
                    canvas.create_text(
                        207.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="4am_temp")
                elif time_slot == "8am":
                    canvas.delete("8am_temp")
                    canvas.create_text(
                        352.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="8am_temp")
                elif time_slot == "12pm":
                    canvas.delete("12pm_temp")
                    canvas.create_text(
                        483.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="12pm_temp")
                elif time_slot == "4pm":
                    canvas.delete("4pm_temp")
                    canvas.create_text(
                        615.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="4pm_temp")
                elif time_slot == "8pm":
                    canvas.delete("8pm_temp")
                    canvas.create_text(
                        735.0,
                        633.0,
                        anchor="nw",
                        text=temp,
                        fill="#221D1D",
                        font=("Inter SemiBold", 12 * -1),
                        tags="8pm_temp")

        else:
            canvas.delete("location_text")  # Delete previous location text
            canvas.create_text(
                345.0,
                220.0,
                anchor="nw",
                text="City not found",
                fill="#221D1D",
                font=("Inter SemiBold", 20 * -1),
                tags="location_text")
            canvas.delete("temperature_text")
            canvas.create_text(
                265.0,
                220.0,
                anchor="nw",
                text=" Error",
                fill="#221D1D",
                font=("Inter", 140),
                tags="temperature_text")
            canvas.delete("humidity_txt")
    else:
        canvas.delete("location_text")  # Delete previous location text
        canvas.create_text(
            340.0,
            215.0,
            anchor="nw",
            text="Enter a city name",
            fill="#221D1D",
            font=("Inter SemiBold", 20 * -1),
            tags="location_text")
        canvas.delete("temperature_text")
        canvas.create_text(
            265.0,
            220.0,
            anchor="nw",
            text=" Error",
            fill="#221D1D",
            font=("Inter", 140),
            tags="temperature_text")
        canvas.delete("humidity_txt")
# Create and configure the main window
window = Tk()
window.title("Weather App")
window.geometry("820x658")
window.configure(bg = "#B2CBF0")

# Create the main canvas for the UI
canvas = Canvas(
    window,
    bg = "#B2CBF0",
    height = 658,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# Create sidebar rectangle for 7-day forecast
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    628.0,
    18.0,
    802.0,
    486.0,
    fill="#ACC4E7",
    outline="")

# Add app logo
image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    54.0,
    50.0,
    image=image_image_16)

# Create hourly forecast sections (12 AM to 8 PM)
# 12 AM section
canvas.create_text(
    70.0,
    550.0,
    anchor="nw",
    text="12 am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    70.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="12am_temp")
image_image_1 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_1 = canvas.create_image(
    81.0,
    600.0,
    image=image_image_1)

# 4 AM section
canvas.create_text(
    207.0,
    550.0,
    anchor="nw",
    text="4 am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    207.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="4am_temp")
image_image_11 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_11 = canvas.create_image(
    223.0,
    600.0,
    image=image_image_11)

# 8 AM section
canvas.create_text(
    350.0,
    550.0,
    anchor="nw",
    text="8 am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    352.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="8am_temp")
image_image_4 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_4 = canvas.create_image(
    363.0,
    600.0,
    image=image_image_4)

# 12 PM section
canvas.create_text(
    480.0,
    550.0,
    anchor="nw",
    text="12 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    483.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="12pm_temp")
image_image_9 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_9 = canvas.create_image(
    499.0,
    600.0,
    image=image_image_9)

# 4 PM section
canvas.create_text(
    615.0,
    550.0,
    anchor="nw",
    text="4 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    615.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="4pm_temp")
image_image_7 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_7 = canvas.create_image(
    623.0,
    600.0,
    image=image_image_7)

# 8 PM section
canvas.create_text(
    735.0,
    550.0,
    anchor="nw",
    text="8 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    735.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="8pm_temp")
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_image_6 = image_image_6.subsample(2)
image_6 = canvas.create_image(
    750.0,
    600.0,
    image=image_image_6)

# Create sunset information display
canvas.create_text(
    154.0,
    236.0,
    anchor="nw",
    text="12 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags="sunset_time")
canvas.create_text(
    100.0,
    236.0,
    anchor="nw",
    text="Sunset : ",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    55.0,
    232.0,
    image=image_image_14
)

# Create sunrise information display
canvas.create_text(
    154.0,
    140.0,
    anchor="nw",
    text="12 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags="sunrise_time")
canvas.create_text(
    100.0,
    140.0,
    anchor="nw",
    text="Sunrise :",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    54.0,
    139.0,
    image=image_image_13)

# Create wind speed information display
canvas.create_text(
    99.0,
    431.0,
    anchor="nw",
    text="Current wind speed :",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    220.0,
    431.0,
    anchor="nw",
    text="12 m/s",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="wind_speed_txt")
image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    55.0,
    439.0,
    image=image_image_18
)

# Create humidity information display
canvas.create_text(
    99.0,
    332.0,
    anchor="nw",
    text="Current humidity :",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
canvas.create_text(
    203.0,
    332.0,
    anchor="nw",
    text="20 %",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="humidity_txt")
image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    55.0,
    340.0,
    image=image_image_17
)

# Create 7-day forecast section header
canvas.create_text(
    665.0,
    30.0,
    anchor="nw",
    text="7-day forecast",
    fill="#221D1D",
    font=("Helvetica", 14))

# Create daily forecast entries (Sunday through Saturday)
# Sunday
canvas.create_text(
    705.0,
    83.0,
    anchor="nw",
    text="Sunday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    672.0,
    93.0,
    image=image_image_15)

# Monday
canvas.create_text(
    703.0,
    143.0,
    anchor="nw",
    text="Monday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    672.0,
    147.0,
    image=image_image_2)

# Tuesday
canvas.create_text(
    705.0,
    200.0,
    anchor="nw",
    text="Tuesday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    672.0,
    210.0,
    image=image_image_12)

# Wednesday
canvas.create_text(
    705.0,
    260.0,
    anchor="nw",
    text="Wednesday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    672.0,
    268.0,
    image=image_image_3)

# Thursday
canvas.create_text(
    705.0,
    321.0,
    anchor="nw",
    text="Thursday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    672.0,
    335.0,
    image=image_image_10)

# Friday
canvas.create_text(
    705.0,
    384.0,
    anchor="nw",
    text="Friday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    672.0,
    395.0,
    image=image_image_5)

# Saturday
canvas.create_text(
    705.0,
    450.0,
    anchor="nw",
    text="Saturday",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    671.0,
    451.0,
    image=image_image_8)

# Create main display elements (Location, Temperature, Rain Chance)
#Current location
canvas.create_text(
    370.0,
    215.0,
    anchor="nw",
    text="Location",
    fill="#221D1D",
    font=("Inter SemiBold", 20 * -1),
    tags="location_text"
)
# Display current temperature
canvas.create_text(
    265.0,
    220.0,
    anchor="nw",
    text="75°F",
    fill="#221D1D",
    font=("Inter", 140),
    tags="temperature_text"
)
canvas.create_text(
    334.0,
    390.0,
    anchor="nw",
    text="Chances of rain: 40%",
    fill="#221D1D",
    font=("Inter SemiBold", 20 * -1),
    tags="rain_chance_txt")




current_day = datetime.now().strftime('%A')
canvas.create_text(
    360.0,
    500.0,
    anchor="nw",
    text=f"{current_day}'s forecast",
    fill="#221D1D",
    font=("Helvetic", 15)
)

# Create search interface elements
# Search bar
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    413.0,
    43.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D2E1F7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=265.0,
    y=21.0,
    width=267.0,
    height=45.0
)

# Search button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: search_weather(),  # Fixed the command callback
    relief="flat"
)
button_1.place(
    x=344.0,
    y=89.0,
    width=131.0,
    height=40.0
)

# Configure window properties and start main loop
window.resizable(False, False)
window.mainloop()