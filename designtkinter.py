import tkinter as tk


# Function to convert a color name to an (R, G, B) tuple
def name_to_rgb(color_name):
    r, g, b = root.winfo_rgb(color_name)  # Convert color name to RGB values using Tkinter's winfo_rgb
    return (r // 256, g // 256, b // 256)  # Scale the values from 0-65535 to 0-255


# Function to convert an (R, G, B) tuple to hex color string
def rgb_to_hex(rgb_color):
    return f'#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}'


# Function to calculate brightness (luminance) of a color
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
        listbox.config(bg=current_color, fg=text_color)
        label_temp.config(bg=current_color, fg=text_color)
        label_condition.config(bg=current_color, fg=text_color)

        # Schedule next color change
        root.after(delay, step_color_change, step + 1)

    # Start the color transition
    step_color_change(0)


# Sample weather data using color names
weather_data = {
    "Monday": {"Temp": "25°C", "Condition": "Sunny", "Color": "lightyellow"},  # LightYellow
    "Tuesday": {"Temp": "22°C", "Condition": "Cloudy", "Color": "lightgray"},  # LightGray
    "Wednesday": {"Temp": "18°C", "Condition": "Rainy", "Color": "lightblue"},  # LightBlue
    "Thursday": {"Temp": "20°C", "Condition": "Partly Cloudy", "Color": "lightgreen"},  # LightGreen
    "Friday": {"Temp": "26°C", "Condition": "Sunny", "Color": "lightyellow"}  # LightYellow
}

# Create the main application window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("300x300")

# Label to display weather details
label_temp = tk.Label(root, text="Temperature: ", font=("Helvetica", 14), bg='#FFFFFF', fg='black')
label_temp.pack(pady=10)
label_condition = tk.Label(root, text="Condition: ", font=("Helvetica", 14), bg='#FFFFFF', fg='black')
label_condition.pack(pady=10)


# Function to handle day selection
def on_day_selected(event):
    selected_day = listbox.get(listbox.curselection())
    weather_info = weather_data[selected_day]

    # Update weather details
    label_temp.config(text=f"Temperature: {weather_info['Temp']}")
    label_condition.config(text=f"Condition: {weather_info['Condition']}")

    # Get the new background color and initiate smooth transition
    new_color = weather_info['Color']
    current_color = root.cget('bg')

    # Convert color names to RGB tuples for both current and new color
    start_rgb = name_to_rgb(current_color)
    end_rgb = name_to_rgb(new_color)

    # Smoothly transition from current color to new color
    smooth_transition(start_rgb, end_rgb)


# Listbox to select a day
listbox = tk.Listbox(root, font=("Helvetica", 14))
for day in weather_data.keys():
    listbox.insert(tk.END, day)
listbox.pack(pady=20)

# Bind selection event to the listbox
listbox.bind('<<ListboxSelect>>', on_day_selected)

# Start the application with a default background color (white)
root.config(bg='#FFFFFF')
listbox.config(bg='#FFFFFF', fg='black')

root.mainloop()
