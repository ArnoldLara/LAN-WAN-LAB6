from random import randint
from random import seed
import time

temp_inf=0
temp_sup=50

print('Los limites de temperatura varian entre ', temp_inf, 'y' ,temp_sup)

seed(0)

for x in range(0, 10):
    #Generar numeros aleatorios
    temp = randint(int(temp_inf),int(temp_sup))
    print(temp)

    if temp<25:
        print('LED-GREEN')
    else:
        print('LED-RED')

    time.sleep(1)
