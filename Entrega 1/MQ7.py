import RPi.GPIO as GPIO, time
 
# Declaramos
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)

 
# Cuerpo del código
try:
    while True:
        if GPIO.input(15)<=1:
        	print("Sin problemas")
        	time.sleep(0.2)
        else:
        	print("GASSSSSS")
        	time.sleep(0.1)
        	

# Cerramos el script
except KeyboardInterrupt:
    GPIO.cleanup()