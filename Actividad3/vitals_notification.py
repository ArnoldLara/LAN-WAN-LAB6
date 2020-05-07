#Include the Beebotte SDK for Python
from beebotte import *
import statistics
import sender_email
import blinking_led

bclient = BBT("RTuCupjAtBf6Ica9wLSXIwWi", "XfVtQRTeiE5jwjz4eUBchXuUTBZHbRpY")


rec1 = Resource(bclient,'Signos_vitales','Glucosa')
rec2 = Resource(bclient,'Signos_vitales','Temperatura')
rec3 = Resource(bclient,'Signos_vitales','Oxigeno')

if input("Desea recibir un email por estado de alerta: (S)(N)") == 'S':
    receiver_email=input("Ingrese su correo electronico: ")
    email=True
    blinking_email.led('RED',True)
else:
    email=False
    blinking_email.led('GREEN',True)

while True:
    gluc_list = rec1.read(limit = 5)
    temp_list = rec2.read(limit = 5)
    oxi_list = rec3.read(limit = 5)
    #print(temp_list)
    gluc= [gluc_list[0]['data'],gluc_list[1]['data'],gluc_list[2]['data']]
    temp = [temp_list[0]['data'],temp_list[1]['data'],temp_list[2]['data']]
    oxi = [oxi_list[0]['data'],oxi_list[1]['data'],oxi_list[2]['data']]

    print('Glucosa:', gluc[2],'mg/dl ','Temperatura:',"%.2f" % temp[2],'°','Oxigeno:',oxi[2],'%')
    print('Glucosa:', gluc[1],'mg/dl ','Temperatura:',"%.2f" % temp[1],'°','Oxigeno:',oxi[1],'%')
    print('Glucosa:', gluc[0],'mg/dl ','Temperatura:',"%.2f" % temp[0],'°','Oxigeno:',oxi[0],'%')

    alerta=False
    glucosa=0
    gluc_mean = statistics.mean(gluc)

    if gluc_mean < 108:
        glucosa = 'Glucosa: Normal ( < 108 mg/dl )'
    elif gluc_mean >=108 and gluc_mean <= 125:
        glucosa = 'Glucosa: Prediabetes( 108 – 125 mg/dl )'
    elif gluc_mean >=126:
        alerta=True
        glucosa = 'Glucosa: Diabetes( < 126 mg/dl)'

    temperatura=0
    temp_mean = statistics.mean(temp)
    #print(temp_mean)
    if temp_mean >= 35 and temp_mean <= 37:
        temperatura = 'Temperatura: Normal (35 – 37 grados centigrados)'
    elif temp_mean >= 37.1 and temp_mean <= 37.9:
        temperatura = 'Temperatura: Estado febril (37.1 - 37.9 grados centigrados)'
    elif temp_mean >=38:
        alerta=True
        temperatura = 'Temperatura: Fiebre (38 - 40 grados centigrados)'

    oxigeno=0
    oxi_mean = statistics.mean(oxi)
    if oxi_mean >= 95 and oxi_mean <= 99:
        oxigeno = 'SPO2: Normal (95% – 99%)'
    elif oxi_mean >= 91 and oxi_mean <= 94:
        oxigeno = 'SPO2: Bajo nivel(91% - 94%)'
    elif oxi_mean <=90:
        alerta=True
        oxigeno = 'SPO2: Problemas de respiración o circulación (< 90%)'

    print(glucosa, temperatura, oxigeno)


    if email and alerta:
        sender_email.envio_email(receiver_email,glucosa,temperatura,temperatura)
        break
    elif alerta:
        print('ALERTA HAY UNA CONDICIÓN CRITICA.')
        alerta = False



    # if int(temp)<25:
    #     print('LED-GREEN')
    # else:
    #     print('LED-RED')

    #time.sleep(1)
