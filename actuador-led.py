from random import randint
from random import seed
import time

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")

# temp_inf=0
# temp_sup=50
# print('Los limites de temperatura varian entre ', temp_inf, 'y' ,temp_sup)

# seed(0)

recurso = Resource(bclient,'Escenario1','Sensor1')


while True:
    temp_list = recurso.read(limit = 5)
    #print(temp_list)
    temp_dict = temp_list[0]
    temp = temp_dict['data']
    print("Temperatura recibida: ",temp)

    if int(temp)<25:
        print('LED-GREEN')
    else:
        print('LED-RED')

    #time.sleep(1)
