# Import required libraries
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Set up path handling for assets/images
SCRIPT_DIR = Path(__file__).parent.absolute()
ASSETS_PATH = SCRIPT_DIR / "assets"

# Helper function to construct paths to asset files
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    509.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    81.0,
    573.0,
    image=image_image_1)

# 4 AM section
canvas.create_text(
    207.0,
    509.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    223.0,
    583.0,
    image=image_image_11)

# 8 AM section
canvas.create_text(
    350.0,
    509.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    363.0,
    583.0,
    image=image_image_4)

# 12 PM section
canvas.create_text(
    480.0,
    509.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    499.0,
    583.0,
    image=image_image_9)

# 4 PM section
canvas.create_text(
    615.0,
    509.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    623.0,
    575.0,
    image=image_image_7)

# 8 PM section
canvas.create_text(
    735.0,
    515.0,
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
    font=("Inter SemiBold", 12 * -1))
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    750.0,
    583.0,
    image=image_image_6)

# Create sunset information display
canvas.create_text(
    154.0,
    236.0,
    anchor="nw",
    text="12 pm",
    fill="#221D1D",
    font=("Inter SemiBold", 12 * -1))
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
    font=("Inter SemiBold", 12 * -1))
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
    font=("Inter SemiBold", 12 * -1))
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
    font=("Inter SemiBold", 12 * -1))
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
canvas.create_text(
    370.0,
    200.0,
    anchor="nw",
    text="Location",
    fill="#221D1D",
    font=("Inter SemiBold", 20 * -1)
)
# Display current temperature
canvas.create_text(
    250.0,
    200.0,
    anchor="nw",
    text="72°F",
    fill="#221D1D",
    font=("Inter", 170)
)
canvas.create_text(
    334.0,
    390.0,
    anchor="nw",
    text="Chances of rain: 40%",
    fill="#221D1D",
    font=("Inter SemiBold", 20 * -1)
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
    command=lambda: print("button_1 clicked"),
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