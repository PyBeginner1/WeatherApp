from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.geometry("400x75")
root.title("Weather App")

def zipLookup():

    try:
        api_req=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=50&API_KEY=****")
        api = json.loads(api_req.content)           #converts json to python
        city = api[0]["ReportingArea"]
        quality =str(api[0]["AQI"])
        category= api[0]["Category"]["Name"]

        #creating bg color based on category i.e good(green), bad(yelow)...
        if category == 'Good':
            weather_color = '#00E400'
        elif category == 'Moderate':
            weather_color = '#ffff00'
        elif category == 'Unhealthy for Sensitive Groups ':
            weather_color = '#ff7e00'
        elif category == 'Unhealthy':
            weather_color = '#ff0000'
        elif category == 'Very Unhealthy':
            weather_color = '#8F3F97'
        elif category == 'Hazardous':
            weather_color = '#7E0023'

        root.configure(background=weather_color)

        mylabel = Label(root, text=city + "  Air Quality:" + quality + "  Category:" + category,font=('Shanti', 15),background=weather_color)  # there are 3 lists so displaying only the 1st one
        mylabel.grid(row=1, column=0)
    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0)

zipButton = Button(root, text='Zipcode', command=zipLookup)
zipButton.grid(row=0, column=1)



root.mainloop()