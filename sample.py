from tkinter import *



def __init__():
    # create root window
    root = Tk()

    # create a horizontal scrollbar (orient set to horizontal)
    h = Scrollbar(root, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)

    # create a vertical scrollbar (default is vertical)
    v = Scrollbar(root)
    v.pack(side=RIGHT, fill=Y)

    # create a Text widget with no line wrapping (wrap=NONE)
    t = Text(root, width=40, height=20, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    # insert some text into the Text widget
    for i in range(100):
        t.insert(END, f"This is line number {i + 1}\n")

    t.pack(side=TOP, fill=BOTH, expand=True)

    # configure the horizontal and vertical scrollbars
    h.config(command=t.xview)
    v.config(command=t.yview)

    # Function to handle scrolling with the touchpad/mouse wheel
    def on_mouse_wheel(event):
        # For macOS, event.delta is very small, so no need to divide it
        t.yview_scroll(-1 * int(event.delta / 120), "units")

    # Function to scroll using the keyboard arrow keys
    def on_key_press(event):
        if event.keysym == "Up":
            t.yview_scroll(-1, "units")  # Scroll up
        elif event.keysym == "Down":
            t.yview_scroll(1, "units")  # Scroll down
        elif event.keysym == "Left":
            t.xview_scroll(-1, "units")  # Scroll left
        elif event.keysym == "Right":
            t.xview_scroll(1, "units")  # Scroll right

    # Bind mouse wheel event (for touchpad scrolling on macOS)
    root.bind_all("<MouseWheel>", on_mouse_wheel)

    # Bind arrow keys for scrolling
    root.bind("<Up>", on_key_press)
    root.bind("<Down>", on_key_press)
    root.bind("<Left>", on_key_press)
    root.bind("<Right>", on_key_press)

    # Start the Tkinter event loop
    root.mainloop()
__init__()

# create an object of ScrollBar class to run the application

