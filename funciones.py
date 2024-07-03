import os
import time
import msvcrt
import csv
ruta=[{"Santiago", "Paine", "Buin"}]
cilindr=[]
cilindro=[]
run=[]
client=[]
direcci=[]
comun=[]
pedidos=[]             
def opcio_1():
     while True:
        os.system("cls")
        try:
            rut=int(input("(Si es guión K, remplaze por un 1!) Ingrese su rut: "))
            if rut<0:
                print("No puede ingresar numeros negativos")
            else:
                break
            run.append(rut)
        except:
            print("NO PUEDE INGRESAR CARACTERES!!")
            nombre=input("Ingrese su nombre: ")
            client.append(nombre)
            direccion=input("Ingrese su direccion: ")
            direcci.append(direccion)
            comuna=input("Ingrese su comuna: ")
            comun.append(comuna)
        while True:
            os.system("cls")
            print(f"""Detalle del pedido
                1, Cilindro de 5 kilos ($12.500 C/U)
                2, Cilindro de 15 kilos ($25.500 C/U)""")
            try:
                pedido=int(input("Ingrese una opción: "))
                if pedido>=1 and pedido<=2:
                    pass
                else:
                    print("ERROR NO PUEDE INGRESAR NUMEROS QUE NO ESTAN EN LAS OPCIÓNES!")
            except:
                print("NO INGRESE CARACTERES!!")
            if pedido== 1: 
                 while True:
                    os.system("cls")
                    try:
                        cantidad=int(input("Ingrese  cuanto quiere: "))
                        if cantidad>=0:
                            pass
                        else:
                            print("ERROR NO INGRESE NUMEROS NEGATIVOS!!")
                    except:
                        print("NO INGRESE CARACTERES!!")
                        prec=cantidad*5
                        prefinal=prec*12500
                        cilindr.append(prefinal)
                        respu=input("¿Quiere seguir agregando? si/no: ")
                        if respu=="si":
                            return
                        else:
                            break
            elif pedido==2:
                while True:
                    os.system("cls")
                    try:
                        cantidad=int(input("Ingrese cuantos quiere: "))
                        if cantidad>=0:
                            pass
                        else:
                            print("ERROR NO INGRESE NUMEROS NEGATIVOS!!")
                    except:
                        print("NO INGRESE CARACTERES!!")
                    prec=cantidad*15
                    prefinal=prec*25500
                    cilindro.append(prefinal)
                    respu=input("¿Quiere seguir agregando? si/no: ")
                    if respu=="si":
                       return
                    else:
                        break
            pedidos.append(f"""   RUT   Cliente    Dirección    Comuna     Cil.5kg      Cil.15kg
                                 {run}  {client}   {direcci}    {comun}   {cilindr}    {cilindro}""")  

def opcio_2():
    os.system("cls")
    print("Aqui estan todos los pedidos realizados")
    for x in pedidos:
        print(x)
        print("Presione una tecla para continuar!")
        msvcrt.getch()

def opcio_3():
    rutt=int(input("(Si es guión K, remplaze por un cero!) Ingrese RUT: "))
    for rutt in run :
        print(rutt)        

def opcio_4():
    while True:
        print("""RUTAS
        1, Santiago
        2, Buin
        3, Paine""")
        ruta=int(input("Seleccione una ruta!"))






