import tkinter as tk
import requests
import time

def getWeather(canvas):
    #get the text from your entry field
    city = textfield.get()
    api='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ad72881d81feb3b1004999c9ae18c7d6'
    json_data = requests.get(api).json()
    #reading from json data file
    #returns if its sunny, cloudy, rainy
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)      #to convert K to Celsius
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    #pressure
    pressure = json_data['main']['pressure']
    #humidity
    humidity = json_data['main']['humidity']
    #wind
    wind = json_data['wind']['speed']
    #IST timezone-GMT +5:30, so convert it into secs gives 19800
    sunrise =time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] -19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data ['sys']['sunset'] -19800))

    final_info = condition + '\n' + str(temp) + '°C'
    final_data = 'Min Temperature:' + str(min_temp) + '\n' +  "Max Temperature:" + str(max_temp) + '\n' + 'Pressure:' + str(pressure) + '\n' + 'Humidity: ' + str(humidity) + '\n' + "Wind:" + str(wind) + '\n' + 'Sunrise:' + sunrise + '\n' + 'Sunset:' + sunset
    label1.config(text =final_info )
    label2.config(text = final_data)




canvas = tk.Tk()
canvas.geometry('500x400')
canvas.title('Weather App')

f = ('Shanti', 15, 'bold')
t = ('Shanti', 35, 'bold')

#to enter city
textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20, padx = 20)
#on hitting enter key
textfield.bind("<Return>", getWeather)

#label
label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()



canvas.mainloop()