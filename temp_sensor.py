from random import randint
from random import seed
import time

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")

print('Simulador de Sensor de temperatura')
print('Ingrese temperatura inferior')
temp_inf=input()
print('Ingrese temperatura superior')
temp_sup=input()

print('Los limites de temperatura varian entre ', temp_inf, 'y' ,temp_sup)

#Iniciar semilla
seed(0)


## Or simply
#bclient.write('Escenario1', 'Sensor1', '25')

for x in range(0, 10):
    #Generar numeros aleatorios
    temp = randint(int(temp_inf),int(temp_sup))
    bclient.write('Escenario1', 'Sensor1', temp)
    print(temp)
    #time.sleep(0.5)
