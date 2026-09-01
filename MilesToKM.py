# Widgets: text, buttons, entry field(input)
#Layout: top to bottom or left to right or as we wish
# Style: as it suggests

import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()    #window object(for the window of app)
window.title("First App")   #title
window.geometry("300x300")  #window
window.config(bg="pink")    #background

#widget
#title
title_label = ttk.Label(master = window, text = "Miles to Km", font="Calibri 24 bold italic")
#master: the object we need to place the text in
#text: text to show
#But, we need pack method to display on app's window
title_label.pack(pady=10)   #pady to add pixels top/bottom

#input field
input_label = ttk.Label(master = window, text = "Enter Miles:")
input_label.pack(pady=10)
entry = ttk.Entry(window)
entry.pack(pady=5)

#conversion function
def convert():
    miles = float(entry.get())
    km = miles*1.60934
    input_label.config(text=f"{miles} Miles = {km:.2f} Km", font = "Calibri 17 italic")

#button, with convert function as command
ttk.Button(master = window, text="Convert", command=convert).pack(pady=10)

#run
window.mainloop()   #to create a window using the window object