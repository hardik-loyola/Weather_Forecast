import tkinter as tk
from tkinter import ttk
import random

from pyasn1.type.univ import Choice

window=tk.Tk()
window.title("HI")
window.geometry("300x300")
canvas=tk.Canvas(window,bg="blue",scrollregion=(0,0,700,700))
canvas.pack(expand=True,fill="both")
for i in range(100):
    l=random.randint(1,700)
    t=random.randint(1,700)
    r=l+random.randint(1,200)
    b=t+random.randint(1,200)
    color= random.choice(("red", "green", "black", "purple"))
    canvas.create_rectangle(l,t,r,b,fill=color)
#mouse y scroll
canvas.bind("<MouseWheel>", lambda event:canvas.yview_scroll(int(event.delta*-1),"units"))

#scroll y
scroll=ttk.Scrollbar(window,orient="vertical",command=canvas.yview)
scroll.place(relx=1,rely=0,relheight=1,anchor="ne")
canvas.configure(yscrollcommand=scroll.set)

#scroll x
scroll1=ttk.Scrollbar(window,orient="horizontal",command=canvas.xview)
scroll1.pack(side="bottom",fill="x")
canvas.configure(xscrollcommand=scroll1.set)
#mouse x scroll
canvas.bind("<Command MouseWheel>", lambda event:canvas.xview_scroll(int(event.delta*-1),"units"))
window.mainloop()