from scipy.misc import electrocardiogram
import time

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")

#Base de datos ECG
ecg = electrocardiogram()


## Or simply
#bclient.write('Escenario1', 'Sensor1', '25')

for i in range(len(ecg)):
    #Generar numeros aleatorios
    valor = ecg[i]
    print(valor)
    bclient.write('Integracion', 'ECG', valor)

    #time.sleep(0.5)
