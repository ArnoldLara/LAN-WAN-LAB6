import random
from random import randint
from random import seed
import time

#Include the Beebotte SDK for Python
from beebotte import *

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")

print('Glucosa')
# print("Los azúcares que se ingieren con los alimentos son transformados por el metabolismo en glucosa.\n"
#     "Ésta se desplaza a través del torrente sanguíneo hasta alcanzar las células de diferentes tipos de tejido proporcionando la energía que necesitan para funcionar.\n"
#     "El simulador usara la medida de mg/dl(miligramos por decilitro) y tomara medidas de pruebas realizadas en ayunas.\n")

print("Seleccione algún estado para generar valores en el correspondiente rango de valores.\n")
print(' (1) Normal ( < 108 mg/dl )\n'
      ' (2) Prediabetes( 108 – 125 mg/dl )\n'
      ' (3) Diabetes( < 126 mg/dl )\n'
      ' (4) Aleatorio (108 – 200 mg/dl )\n')
#Valores de Glocusa
glucosa=[0,{'gluc_inf':50,'gluc_sup':107},
           {'gluc_inf':108,'gluc_sup':125},
           {'gluc_inf':126,'gluc_sup':150},
           {'gluc_inf':50,'gluc_sup':150},]

while True:
    valor_gluc=input()
    if valor_gluc >= '1' and valor_gluc <= '4':
        break
    else:
        print("Selecciona un valor valido.\n")


print('Temperatura Corporal \n')
# print("La temperatura corporal es un indicador que evalúa la regulación térmica de nuestro organismo.\n"
#     "La temperatura normal de una persona esta entre 35 y 37 grados centígrados. \n"
#     "Valores de temperatura entre 37.1 y 37.9 ° centígrados indican un estado febril y valores por encima de 38 grados indican un estado de hipertermia o fiebre.\n")

print("Seleccione algún estado para generar valores en el correspondiente rango de valores.\n")
print(' (1) Normal (35° – 37° centigrados)\n'
      ' (2) Estado febril (37.1° - 37.9 °  centígrados)\n'
      ' (3) Fiebre (38° - 40° centígrados)\n'
      ' (4) Aleatorio (35° - 42°)\n')
#Valores de Glocusa
temperatura=[0,{'temp_inf':35,'temp_sup':37},
               {'temp_inf':37.1,'temp_sup':37.9},
               {'temp_inf':38,'temp_sup':40},
               {'temp_inf':35,'temp_sup':42},]

while True:
    valor_temp=input()
    if valor_temp >= '1' and valor_temp <= '4':
        break
    else:
        print("Selecciona un valor valido.\n")




print('Oxigeno en la sangre \n')
# print("El oxigeno en la sangre es una medida de cuanto oxigeno transporta la sangre de una persona. \n"
#     "Esta es medida por un pulsioxímetro. Cuando respiramos, nuestros pulmones inhalan oxígeno y exhalan dióxido de carbono.\n"
#     "El desequilibrio entre los niveles de oxígeno y dióxido de carbono en la sangre puede ser un signo de que los pulmones no están funcionando bien.\n")

print("Seleccione algún estado para generar valores en el correspondiente rango de valores.\n")
print(' (1) Normal (95% – 99% )\n'
      ' (2) Bajo nivel(91% - 94%)\n'
      ' (3) Problemas de respiración o circulación (< 90%)\n'
      ' (4) Aleatorio (1% - 99%)\n')
#Valores de Glocusa
oxigeno=[0,{'oxi_inf':95,'oxi_sup':99},
           {'oxi_inf':91,'oxi_sup':94},
           {'oxi_inf':1,'oxi_sup':90},
           {'oxi_inf':1,'oxi_sup':99},]

while True:
    valor_oxi=input()
    if valor_oxi >= '1' and valor_oxi <= '4':
        break
    else:
        print("Selecciona un valor valido.\n")



print('El rango de valores de Glucosa variara entre ', glucosa[int(valor_gluc)]['gluc_inf'], 'mg/dl y' ,glucosa[int(valor_gluc)]['gluc_sup'], 'mg/dl ')
print('El rango de valores de temperatura corporal variara entre ', temperatura[int(valor_temp)]['temp_inf'],'° y' ,temperatura[int(valor_temp)]['temp_sup'],'°')
print('El rango de valores de oxigeno en sangre variara entre ', oxigeno[int(valor_oxi)]['oxi_inf'],'% y' ,oxigeno[int(valor_oxi)]['oxi_sup'],'%')

# print('Temperatura corporal')
# temp_inf=37.1
# temp_sup=37.9
#
# print('Rango ', temp_inf, 'y' ,temp_sup)
#
# print('Oxigeno en la sangre')
# oxi_inf=91
# oxi_sup=94
#
# print('Rango ', oxi_inf, 'y' ,oxi_sup)


# Iniciar semilla
seed(2)
while True:
    #print('Glucosa ')
    gluc = randint(glucosa[int(valor_gluc)]['gluc_inf'],glucosa[int(valor_gluc)]['gluc_sup'])
    #print(gluc)

    #print('Temperatura corporal ')
    temp = random.uniform(temperatura[int(valor_temp)]['temp_inf'], temperatura[int(valor_temp)]['temp_sup'])
    #print(temp)

    #print('Oxigeno en la sangre')
    oxi = randint(oxigeno[int(valor_oxi)]['oxi_inf'],oxigeno[int(valor_oxi)]['oxi_sup'])
    #print(oxi)

    print('Glucosa:', gluc,'mg/dl ','Temperatura:',"%.2f" % temp,'°','Oxigeno:',oxi,'%')
    bclient.writeBulk('Signos_vitales', [
                    {'resource': 'Glucosa', 'data': gluc},
                    {'resource': 'Temperatura', 'data': temp},
                    {'resource': 'Oxigeno', 'data': oxi},
                    ])
