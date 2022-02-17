from LexicoVentas import LexicoVentas
from Graficadoras import Graficadora
from Generador import Genera
from help import Menu, Leer_Info, Leer_Intrucciones
from LexicoInstrucciones import LexicoInstrucciones
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import ForwardRef

def main():
    txt_data = ""
    txt_intrucciones = ""
    opcion = Menu()
    lexico_intrucciones = None
    while opcion != 5 :
        if opcion == 1:
            txt_data = Leer_Info()
            print(txt_data)
            txt_data1 = txt_data
        if opcion == 2:
            txt_intrucciones = Leer_Intrucciones()
            print(txt_intrucciones)
            txt_intrucciones1 = txt_intrucciones
        elif opcion == 3:
            if txt_data != "" and txt_intrucciones != "":
                lexico_ventas = LexicoVentas(txt_data)
                #lexico_ventas.printTokens()
                lexico_ventas.GuardarDatos()
                lexico_intrucciones = LexicoInstrucciones(txt_intrucciones)
                #lexico_intrucciones.printTokens()
                lexico_intrucciones.GuardarDatos()
                prueb = Graficadora.general()
                #LexicoVentas.ordenamiento()

            else:
                print("no ha cargado un archivo")
        elif opcion ==4:
            if txt_data != "" and txt_intrucciones != "":
                #LexicoVentas.ordenamiento()
                htm = Genera.reporte()
            else:
                print("No ha cargado algun archivo")
        elif opcion == 5:
            print("Terminando el programa...")
        opcion = Menu();

if __name__ == "__main__":
    main()