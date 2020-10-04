Get weather conditions on your pi using API darksky https://darksky.net/dev/docs you need to register and get the API key (it's free)
from urllib2 import urlopen
import json
import time


apikey="yourapikey"
lati =""  #find your latitude and longitude from google maps. 
longi = ""

try:
#get the data from the api website
 url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"
 oldTemp = 0          
#in case the Internet is not working: try it but then use the oldTemp just in case
 try:
  meteo=urlopen(url).read()
  meteo = meteo.decode('utf-8')
  weather = json.loads(meteo)        
  currentTemp = weather['currently']['temperature']        
  condition = weather['currently']['icon']
  wind = weather['currently']['windSpeed']
 except IOError:           
  currentTemp = oldTemp
    
  oldTemp = currentTemp #set oldTemp to last known temperature

 print currentTemp
 print condition
 print wind
 
 #Weather conditions will be written on a file txt
 mytemp=str(condition) +" "+ str(currentTemp)+" "+str(wind)
 file = open('temp.txt','w') 
 
 file.write(mytemp) 
 
 
 #use different colour LED to display temperature (e.g. red if temperature over 25C, yellow if temperature over 17C etc..."
 
 if 0 < currentTemp < 10:
  GPIO.output(27,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW) 
  GPIO.output(22,GPIO.LOW) 
  GPIO.output(24,GPIO.LOW)
 
 if 10 < currentTemp < 17:
  GPIO.output(24,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  GPIO.output(22,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)

 if 17 < currentTemp < 25:
  GPIO.output(23,GPIO.HIGH)
  GPIO.output(24,GPIO.LOW)
  GPIO.output(22,GPIO.LOW) 
  GPIO.output(27,GPIO.LOW)

 if currentTemp > 25: 
  GPIO.output(22,GPIO.HIGH)
  GPIO.output(23,GPIO.LOW)
  GPIO.output(24,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)

except KeyboardInterrupt:
 print("Exit")
