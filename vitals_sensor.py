import random
from random import randint
from random import seed
import time

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")

print('Glucosa')
gluc_inf=108
gluc_sup=125

print('Rango ', gluc_inf, 'y' ,gluc_sup)

print('Temperatura corporal')
temp_inf=37.1
temp_sup=37.9

print('Rango ', temp_inf, 'y' ,temp_sup)

print('Oxigeno en la sangre')
spo2_inf=91
spo2_sup=94

print('Rango ', spo2_inf, 'y' ,spo2_sup)

## Create a Resource object
# res1 = Resource(bclient, 'Signos_vitales', 'Glucosa')
# res2 = Resource(bclient, 'Signos_vitales', 'Temperatura')
# res3 = Resource(bclient, 'Signos_vitales', 'Oxigeno')

#Iniciar semilla
seed(2)
while True:
    print('Glucosa ')
    gluc = randint(int(gluc_inf),int(gluc_sup))
    print(gluc)

    print('Temperatura corporal ')
    temp = random.uniform(temp_inf, temp_sup)
    print(temp)

    print('Oxigeno en la sangre')
    spo2 = randint(int(spo2_inf),int(spo2_sup))
    print(spo2)

    bclient.writeBulk('Signos_vitales', [
                    {'resource': 'Glucosa', 'data': gluc},
                    {'resource': 'Temperatura', 'data': temp},
                    {'resource': 'Oxigeno', 'data': spo2},
                    ])
