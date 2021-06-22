import requests,sys
#import os
from datetime import datetime

api_key = 'b619c8d8d2ff7dc1104d887b52009d9b'
location = raw_input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("The weather information of the city {} has been written to the file name winfo.txt".format(location))
original_stdout = sys.stdout
with open("winfo.txt","w") as fw:
    #f.write(api_data.text)
    sys.stdout = fw
    print ("*----------*----------*----------*----------*----------*----------*")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("*----------*----------*----------*----------*----------*----------*")
    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  : {} ".format(weather_desc))
    print ("Current Humidity      : {} %".format(hmdt))
    print ("Current wind speed    : {} kmph".format(wind_spd))

sys.stdout = original_stdout
