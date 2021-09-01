import RPi.GPIO as GPIO, time
import Adafruit_DHT  
import time

# Configuración de puertos
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

# Uso DHT
sensor = Adafruit_DHT.DHT11
pin = 4

while True:
# DHT11
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)
  
# MQ-4
    CH4 = GPIO.input(18)
    print ('CH4: ' , CH4)
    if GPIO.input(18)==1:
        print("No se detecta CH4")
        time.sleep(0.2)
    else:
        print("Se detecta CH4")
        time.sleep(0.1)

#MQ-7
    CO = GPIO.input(15)    
    print ('CO: ' , CO)
    if GPIO.input(15)==1:
        print("No se detecta CO")
        time.sleep(0.2)
    else:
        print("Se detecta CO")
        time.sleep(0.1)