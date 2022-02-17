from LexicoVentas import LexicoVentas
from Graficadoras import Graficadora
from help import Menu, Leer_Info, Leer_Intrucciones
from LexicoInstrucciones import LexicoInstrucciones
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import ForwardRef
def main():
    txt_data1 = ""
    txt_intrucciones1 = ""
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
        elif opcion == 3:
            lexico_ventas = LexicoVentas(txt_data)
            lexico_ventas.printTokens()
            lexico_ventas.GuardarDatos()
            lexico_intrucciones = LexicoInstrucciones(txt_intrucciones)
            #lexico_intrucciones.printTokens()
            lexico_intrucciones.GuardarDatos()
        elif opcion ==4:
            prueb = Graficadora.general()
        elif opcion == 5:
            print("Terminando el programa...")
        opcion = Menu();

if __name__ == "__main__":
    main()