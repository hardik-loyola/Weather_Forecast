# Import required libraries
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import requests
import datetime as dt

# Set up path handling for assets/images
SCRIPT_DIR = Path(__file__).parent.absolute()
ASSETS_PATH = SCRIPT_DIR / "assets"

# Helper function to construct paths to asset files
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    520.0,
    anchor="nw",
    text="12am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags="1st")
canvas.create_text(
    70.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="12am_temp")
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    81.0,
    590.0,
    image=image_image_1)

# 4 AM section
canvas.create_text(
    207.0,
    520.0,
    anchor="nw",
    text="4 am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags='2nd')
canvas.create_text(
    207.0,
    633.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),
    tags="4am_temp")
image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    223.0,
    590.0,
    image=image_image_11)

# 8 AM section
canvas.create_text(
    350.0,
    520.0,
    anchor="nw",
    text="8 am",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags='3rd')
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
    590.0,
    image=image_image_4)

# 12 PM section
canvas.create_text(
    480.0,
    520.0,
    anchor="nw",
    text="12 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags='4th')
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
    590.0,
    image=image_image_9)

# 4 PM section
canvas.create_text(
    615.0,
    520.0,
    anchor="nw",
    text="4 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags='5th')
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
    590.0,
    image=image_image_7)

# 8 PM section
canvas.create_text(
    735.0,
    520.0,
    anchor="nw",
    text="8 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1),tags='6th')
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
    590.0,
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
    font=("Inter SemiBold", 12 * -1),tags="1st_day")
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
    font=("Inter SemiBold", 12 * -1),tags="2nd_day")
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
    font=("Inter SemiBold", 12 * -1),tags="3rd_day")
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
    font=("Inter SemiBold", 12 * -1),tags='4th_day')
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
    font=("Inter SemiBold", 12 * -1),tags='5th_day')
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
    font=("Inter SemiBold", 12 * -1),tags='6th_day')
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
    font=("Inter SemiBold", 12 * -1),tags='7th_day')
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




current_day = dt.datetime.now().strftime('%A')
canvas.create_text(
    360.0,
    480.0,
    anchor="nw",
    text=f"{current_day}'s forecast",
    fill="#221D1D",
    font=("Helvetic", 15),tags="day"
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





def get_lat_lon(url_lat):
        response_lat_lon = requests.get(url_lat)
        if response_lat_lon.status_code == 200:
            data = response_lat_lon.json()
            if not data:
                print("no data")
                exit()
            lat=float((data[0]["lat"]))
            lon=float((data[0]["lon"]))
            return lat,lon
        else:
            return 0,0

def url1(lat,lon,api_key):
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,alerts&appid={api_key}&units=imperial'
    response=requests.get(url)
    return response




def current(response):
        if response.status_code == 200:
            data = response.json()
            #temperature
            temp=str(round(int(data["current"]['temp'])))+"°F"
            #wind speed
            wind_speed=str(data["current"]['wind_speed'])+' mph'
            # humidity
            humidity=str(data["current"]['humidity'])+'%'
            #sunrise
            rise = int(data["current"]["sunrise"]) + int(data["timezone_offset"])
            sunrise=dt.datetime.utcfromtimestamp(rise).strftime('%I:%M %p')
            #sunset
            sets = int(data["current"]["sunset"]) + int(data["timezone_offset"])
            sunset=dt.datetime.utcfromtimestamp(sets).strftime('%I:%M %p')

            return temp,wind_speed,humidity,sunrise,sunset
        else:
            print("Error")

def hourly(response,weather_descriptions):
    if response.status_code == 200:

        data = response.json()
        #current time
        time_sam1=int(data['hourly'][0]['dt'])+int(data["timezone_offset"])
        time1=dt.datetime.utcfromtimestamp(time_sam1).strftime('%I %p').strip("0")
        temp1=str(round(data['hourly'][0]['temp']))+"°F"
        #day
        day0 =dt.datetime.utcfromtimestamp(time_sam1).strftime('%A')
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][0]['weather'][0]['description'] in descriptions:
                weather1=weather_type
        #5th hour
        time_sam2 = int(data['hourly'][4]['dt']) + int(data["timezone_offset"])
        time2=dt.datetime.utcfromtimestamp(time_sam2).strftime('%I %p').strip("0")
        temp2 = str(round(data['hourly'][4]['temp']))+"°F"
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][4]['weather'][0]['description'] in descriptions:
                weather2=weather_type
        #9th hour
        time_sam3 = int(data['hourly'][8]['dt']) + int(data["timezone_offset"])
        time3=(dt.datetime.utcfromtimestamp(time_sam3).strftime('%I %p').strip("0"))
        temp3 = str(round(data['hourly'][8]['temp']))+'°F'
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][9]['weather'][0]['description'] in descriptions:
                weather3= weather_type
        #13th hour
        time_sam4 = int(data['hourly'][12]['dt']) + int(data["timezone_offset"])
        time4=(dt.datetime.utcfromtimestamp(time_sam4).strftime('%I %p').strip("0"))
        temp4 = str(round(data['hourly'][12]['temp']))+'°F'
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][12]['weather'][0]['description'] in descriptions:
                weather4= weather_type
        #17th hour
        time_sam5 = int(data['hourly'][16]['dt']) + int(data["timezone_offset"])
        time5=(dt.datetime.utcfromtimestamp(time_sam5).strftime('%I %p').strip("0"))
        temp5 = str(round(data['hourly'][16]['temp']))+'°F'
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][16]['weather'][0]['description'] in descriptions:
                weather5= weather_type
        #21th hour
        time_sam6 = int(data['hourly'][20]['dt']) + int(data["timezone_offset"])
        time6=(dt.datetime.utcfromtimestamp(time_sam6).strftime('%I %p').strip("0"))
        temp6 = str(round(data['hourly'][20]['temp']))+'°F'
        for weather_type, descriptions in weather_descriptions.items():
            if data['hourly'][20]['weather'][0]['description'] in descriptions:
                weather6= weather_type
        chance_of_rain=str(data['hourly'][0]['pop'])+"%"
        return time1,weather1,time2,weather2,time3,weather3,time4,weather4,time5,weather5,time6,weather6,chance_of_rain,temp1,temp2,temp3,temp4,temp5,temp6,day0


def week_forecast(response,weather_descriptions):
    if response.status_code == 200:
        data = response.json()
        # weather for current day
        day1=(dt.datetime.utcfromtimestamp(data['daily'][0]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][0]['weather'][0]['description'] in descriptions:
                day_weather1= weather_type
        # weather for 2nd day
        day2=(dt.datetime.utcfromtimestamp(data['daily'][1]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][1]['weather'][0]['description'] in descriptions:
                day_weather2= weather_type
        # weather for 3rd day
        day3=(dt.datetime.utcfromtimestamp(data['daily'][2]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][2]['weather'][0]['description'] in descriptions:
                day_weather3= weather_type
        # weather for 4th day
        day4=(dt.datetime.utcfromtimestamp(data['daily'][3]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][3]['weather'][0]['description'] in descriptions:
                day_weather4= weather_type
        # weather for 5th day
        day5=(dt.datetime.utcfromtimestamp(data['daily'][4]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][4]['weather'][0]['description'] in descriptions:
                day_weather5= weather_type
        # weather for 6th day
        day6=(dt.datetime.utcfromtimestamp(data['daily'][5]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][5]['weather'][0]['description'] in descriptions:
                day_weather6=(weather_type)
        # weather for 7th day
        day7=(dt.datetime.utcfromtimestamp(data['daily'][6]["dt"]).strftime('%A'))
        for weather_type, descriptions in weather_descriptions.items():
            if data['daily'][6]['weather'][0]['description'] in descriptions:
                day_weather7= weather_type
        return day1,day_weather1,day2,day_weather2,day3,day_weather3,day4,day_weather4,day5,day_weather5,day6,day_weather6,day7,day_weather7


def search_weather():
    weather_descriptions = {
        "clear_weather": ["clear sky"],
        "cloudy_weather": ["overcast clouds"],
        "partly_cloudy_weather":["few clouds","scattered clouds","broken clouds"],
        "rain": ["moderate rain", "heavy intensity rain", "very heavy rain", "extreme rain",
                 "freezing rain", "shower rain", "heavy intensity shower rain", "ragged shower rain"],
        "snow": ["snow", "heavy snow", "sleet", "light shower sleet", "shower sleet",
                 "light rain and snow", "shower snow", "heavy shower snow"],
        "thunderstorm": ["thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain",
                         "light thunderstorm", "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                         "thunderstorm with light drizzle", "thunderstorm with drizzle",
                         "thunderstorm with heavy drizzle"],
        "light_rain": ["light shower rain", "light rain", "light intensity drizzle", "drizzle",
                       "heavy intensity drizzle", "light intensity drizzle rain",
                       "drizzle rain", "heavy intensity drizzle rain", "shower rain and drizzle",
                       "heavy shower rain and drizzle", "shower drizzle", "mist"],
        "light_snow": ["light snow", "rain and snow", "light rain and snow", "light shower snow"],
        "fog": ["fog", "sand", "dust", "sand/dust whirls", "haze", "smoke", "volcanic ash", "squalls"],
        "tornado": ["tornado"]

    }
    city = entry_1.get()

    api_key = 'b5508b18408a1951c9d1e43696eab784'

    url_lat = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'
    lat,lon=get_lat_lon(url_lat)
    response=url1(lat,lon,api_key)
    time1,weather1,time2,weather2,time3,weather3,time4,weather4,time5,weather5,time6,weather6,pop,temp1,temp2,temp3,temp4,temp5,temp6,day0=hourly(response,weather_descriptions,)
    day1,day_weather1,day2,day_weather2,day3,day_weather3,day4,day_weather4,day5,day_weather5,day6,day_weather6,day7,day_weather7=week_forecast(response,weather_descriptions)
    temp,wind_speed,humidity,sunrise,sunset=current(response)
    change_config(time1, weather1, time2, weather2, time3, weather3, time4, weather4, time5, weather5, time6, weather6,
                  day1, day_weather1, day2, day_weather2, day3, day_weather3, day4, day_weather4, day5, day_weather5,
                  day6, day_weather6, day7, day_weather7, temp, wind_speed, humidity, sunrise, sunset,city,pop,temp1,temp2,temp3,temp4,temp5,temp6,day0)
global_images1 = {}
global_images={}
def change_config(time1,weather1,time2,weather2,
                  time3,weather3,time4,weather4,time5,
                  weather5,time6,weather6,day1,day_weather1,
                  day2,day_weather2,day3,day_weather3,day4,day_weather4,
                  day5,day_weather5,day6,day_weather6,day7,day_weather7,temp,wind_speed,humidity,sunrise,sunset,city,pop,temp1,temp2,temp3,temp4,temp5,temp6,day0):

    canvas.delete("temperature_text")  # Delete previous temperature text
    canvas.create_text(
        265.0,
        220.0,
        anchor="nw",
        text=temp,
        fill="#221D1D",
        font=("Inter", 140),
        tags="temperature_text")
    canvas.delete("location_text")  # Delete previous location text
    canvas.create_text(
        370.0,
        215.0,
        anchor="nw",
        text=city.capitalize(),
        fill="#221D1D",
        font=("Inter SemiBold", 20 * -1),
        tags="location_text")
    canvas.delete("humidity_txt")
    canvas.create_text(
        203.0,
        332.0,
        anchor="nw",
        text=humidity,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="humidity_txt")
    canvas.delete("wind_speed_txt")
    canvas.create_text(
        220.0,
        431.0,
        anchor="nw",
        text=wind_speed,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="wind_speed_txt")
    canvas.delete("sunrise_time")
    canvas.create_text(
        154.0,
        140.0,
        anchor="nw",
        text=sunrise,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags="sunrise_time")
    canvas.delete("sunset_time")
    canvas.create_text(
        154.0,
        236.0,
        anchor="nw",
        text=sunset,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags="sunset_time")
    canvas.delete("rain_chance_txt")
    canvas.create_text(
        334.0,
        390.0,
        anchor="nw",
        text=f"Chances of rain: {pop}",
        fill="#221D1D",
        font=("Inter SemiBold", 20 * -1),
        tags="rain_chance_txt")
    canvas.delete("1st")
    canvas.create_text(
        70.0,
        520.0,
        anchor="nw",
        text=time1,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags="1st")
    canvas.delete('12am_temp')
    canvas.create_text(
        70.0,
        633.0,
        anchor="nw",
        text=temp1,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="12am_temp")
    canvas.delete('2nd')
    canvas.create_text(
        207.0,
        520.0,
        anchor="nw",
        text=time2,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags='2nd')
    canvas.delete('4am_temp')
    canvas.create_text(
        207.0,
        633.0,
        anchor="nw",
        text=temp2,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="4am_temp")
    canvas.delete('3rd')
    canvas.create_text(
        350.0,
        520.0,
        anchor="nw",
        text=time3,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags='3rd')
    canvas.delete('8am_temp')
    canvas.create_text(
        352.0,
        633.0,
        anchor="nw",
        text=temp3,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="8am_temp")
    canvas.delete('4th')
    canvas.create_text(
        480.0,
        520.0,
        anchor="nw",
        text=time4,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags='4th')
    canvas.delete('12pm_temp')
    canvas.create_text(
        483.0,
        633.0,
        anchor="nw",
        text=temp4,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="12pm_temp")
    canvas.delete('5th')
    canvas.create_text(
        615.0,
        520.0,
        anchor="nw",
        text=time5,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags='5th')
    canvas.delete('4pm_temp')
    canvas.create_text(
        615.0,
        633.0,
        anchor="nw",
        text=temp5,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="4pm_temp")
    canvas.delete('6th')
    canvas.create_text(
        735.0,
        520.0,
        anchor="nw",
        text=time6,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1), tags='6th')
    canvas.delete("8pm_temp")
    canvas.create_text(
        735.0,
        633.0,
        anchor="nw",
        text=temp6,
        fill="#221D1D",
        font=("Inter SemiBold", 12 * -1),
        tags="8pm_temp")
    canvas.delete('day')
    canvas.create_text(
        360.0,
        480.0,
        anchor="nw",
        text=f"{day0}'s forecast",
        fill="#221D1D",
        font=("Helvetic", 15), tags="day")
    global global_images1
    global_images1.update({
        "clear_weather": PhotoImage(file=relative_to_assets("image_23.png")),
        "cloudy_weather": PhotoImage(file=relative_to_assets("image_1.png")),
        "partly_cloudy_weather": PhotoImage(file=relative_to_assets("image_7.png")),
        "rain": PhotoImage(file=relative_to_assets("image_4.png")),
        "snow": PhotoImage(file=relative_to_assets("image_27.png")),
        "thunderstorm": PhotoImage(file=relative_to_assets("image_9.png")),
        "light_rain": PhotoImage(file=relative_to_assets("image_20.png")),
        "light_snow": PhotoImage(file=relative_to_assets("image_24.png")),
        "fog": PhotoImage(file=relative_to_assets("image_19.png")),
        "tornado": PhotoImage(file=relative_to_assets("image_28.png")),
    })

    if weather1 in global_images1:
        canvas.itemconfig(image_1, image=global_images1[weather1])
    if weather2 in global_images1:
        canvas.itemconfig(image_11, image=global_images1[weather2])
    if weather3 in global_images1:
        canvas.itemconfig(image_4, image=global_images1[weather3])
    if weather4 in global_images1:
        canvas.itemconfig(image_9, image=global_images1[weather4])
    if weather5 in global_images1:
        canvas.itemconfig(image_7, image=global_images1[weather5])
    if weather6 in global_images1:
        canvas.itemconfig(image_6, image=global_images1[weather6])
    global global_images
    global_images.update({
        "clear_weather": PhotoImage(file=relative_to_assets("image_15.png")),
        "cloudy_weather": PhotoImage(file=relative_to_assets("image_2.png")),
        "partly_cloudy_weather":PhotoImage(file=relative_to_assets("image_8.png")),
        "rain": PhotoImage(file=relative_to_assets("image_5.png")),
        "snow": PhotoImage(file=relative_to_assets("image_26.png")),
        "thunderstorm": PhotoImage(file=relative_to_assets("image_10.png")),
        "light_rain": PhotoImage(file=relative_to_assets("image_21.png")),
        "light_snow": PhotoImage(file=relative_to_assets("image_25.png")),
        "fog": PhotoImage(file=relative_to_assets("image_22.png")),
        "tornado": PhotoImage(file=relative_to_assets("image_29.png")),
    })
    if day_weather1 in global_images:
        canvas.itemconfig(image_15, image=global_images[day_weather1])
    if day_weather2 in global_images:
        canvas.itemconfig(image_2, image=global_images[day_weather2])
    if day_weather3 in global_images:
        canvas.itemconfig(image_12, image=global_images[day_weather3])
    if day_weather4 in global_images:
        canvas.itemconfig(image_3, image=global_images[day_weather4])
    if day_weather5 in global_images:
        canvas.itemconfig(image_10, image=global_images[day_weather5])
    if day_weather6 in global_images:
        canvas.itemconfig(image_5, image=global_images[day_weather6])
    if day_weather7 in global_images:
        canvas.itemconfig(image_8, image=global_images[day_weather7])
    




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






