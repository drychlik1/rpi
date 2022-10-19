#DS18B20 - cyfrowy czujnik temperatury
### - PIN GND -> GND
### - PIN DATA -> GPIO.4
### - GPIO.4 -> PIN DATA -> R1 -> 3,3V 
### - R1 = 4,7k OHM
### - PIN V -> 3,3V
### - PIN Data podpinamy do GPIO.4, następnie do płytki wpinamy rezystor (R1), a druga noga R1 do 3,3V

# Sprawdź czy 1-wire jest włączony
lsmod | grep w1
while True

  if False
  import os 
import glob 
import time 

# Te liny holownicze montują urządzenie: 
os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm') 
 
base_dir = '/sys/bus/w1/devices/' 
# Pobierz wszystkie nazwy plików zaczynające się od 28 w ścieżce katalog_bazowy. 
device_folder = glob.glob(base_dir + '28*')[0] 
device_file = device_folder + '/w1_slave' 
def read_rom(): 
    name_file=device_folder+'/name' 
    f = open(name_file,'r') 
    return f.readline () 
 
