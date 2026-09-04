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

#Main Logic Unit
#conversion function
def convert():
    miles = float(entry_value.get())
    km = miles*1.60934
    output_value.set(km)
    

#widget
#title
title_label = ttk.Label(master = window, text = "Miles to Km", font="Calibri 24 bold italic")
#master: the object we need to place the text in
#text: text to show
#But, we need pack method to display on app's window
title_label.pack(pady=25)   #pady to add pixels top/bottom


#input field
input_frame = ttk.Frame(master = window)

#Entry field
entry_value = tk.IntVar()   #to store the value entered in entry widget
entry = ttk.Entry(master = input_frame, textvariable=entry_value)
#textvariable: store values from entery widget to entry_value variable

#Button
button = ttk.Button(master = input_frame, text="Convert", command=convert)
#Remember: don't call the function in the command itself

entry.pack(side="left", padx=10)    #entry field and button along side
button.pack(side="left")
input_frame.pack(pady=10)   #the whole input field and the button


#Output field
output_value = tk.StringVar()
output_label = ttk.Label(master = window, text= "Output",
                         font="Calibri 20", textvariable=output_value)
#The textvariable overrides the text in the label
output_label.pack(pady=10)


#run
window.mainloop()   #to create a window using the window object