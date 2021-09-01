import tkinter as tk
from tkinter import font
from typing import final
import requests
import time




def getWeather(canvas):
    city = textfield.get()
    api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bc3372ff6a955951731421c9cf8ccfa3"
    json_data= requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']) - 273.15

    final_info = "condition" + "\n" + str(condition)
    final_data = "\n" + "Temp: " + str(temp)

    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()

canvas.geometry("600x500")
canvas.title("Weather")

f = ("poppins", 15, "bold")
t = ("poppins", 15, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()