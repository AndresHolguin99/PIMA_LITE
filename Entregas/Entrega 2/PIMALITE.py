# @PIMA LITE
# Pontificia Universidad Javeriana
# 
# Ingeniería Electrónica
# 
# Fundamentos de IoT


# Importa la librería de GPIO.
import RPi.GPIO as GPIO

# Importa la librería SPI, MCP3008 y DHT.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT  

# Importa la librería paho para publicar.
import paho.mqtt.publish as publish
from time import sleep

# Importa la librería para timestamp.
from datetime import datetime
now = datetime.now()


# Configuración de pines tipo BCM.
GPIO.setmode(GPIO.BCM)

# Configuración de puertos.
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

# Configuracion Hardware SPI.
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Configuración DHT.
sensor = Adafruit_DHT.DHT11
pin = 4

while True:
    # Lectura del MCP3008 para los canales 0 y 1
    MQ4 = mcp.read_adc(0)
    MQ7 = mcp.read_adc(1)
    
    # DHT11
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)

    # MQ-4
    CH4 = GPIO.input(18)
    print ('CH4: ' , CH4)
    if GPIO.input(18)==1:
        print("No se detecta CH4")
        sleep(0.2)
    else:
        print("Se detecta CH4")
        sleep(0.1)

    #MQ-7
    CO = GPIO.input(15)    
    print ('CO: ' , CO)
    if GPIO.input(15)==1:
        print("No se detecta CO")
        sleep(0.2)
    else:
        print("Se detecta CO")
        sleep(0.1)
        
    # Almacenamiento de variables
    Temperatura = temperatura
    Humedad = humedad
    Metano = MQ4
    Monoxido = MQ7

    # Creación del Topic de Thingspeak
    topic = "channels/"+"1515522"+"/publish/"+"R3HWFDSTELZGAZP1"

    # Creación del mensaje 
    mensaje = "field1="+str(Temperatura)+"&field2="+str(Humedad)+"&field3="+str(Metano)+"&field4="+str(Monoxido)+"&field5="+str(now)
    try:
        publish.single(topic,payload=mensaje,hostname="mqtt.thingspeak.com",port=1883,tls=None,transport="tcp")
    except:
        print("Error 404")
    sleep(15)
