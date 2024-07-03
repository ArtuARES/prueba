import os
import time
import msvcrt
from funciones import *


while True:
    os.system("cls")
    print(""" Bienvenidos, elija una opción!
    1, Registrar pedidos.
    2, Listar todos los pedidos.
    3, Buscar pedido por RUT.
    4, Imprimir hoja de ruta
    5, Salir del programa""")
    try:
        opc=int(input("Ingrese una opción: "))
        if opc>=1 and opc<=5:
            pass
        else:
            print("ERROR NO DEBE INGRESAR NUMERO QUE NO ESTAN EN LAS OPCIÓNES")
            print("Presione tecla para continuar!")
            msvcrt.getch()
    except:
            print("NO INGRESE CARACTERES!!!")

    if opc==5:
        print("ADIOS, NOS VEMOS PRONTO!")
        break
    elif opc==1:
            opcio_1()
    elif opc==2:
            opcio_2()
    elif opc==3:
            opcio_3()
    else:
            opcio_4()


