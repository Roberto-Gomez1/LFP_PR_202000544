from tkinter import Tk
from tkinter.filedialog import askopenfilename
from typing import ForwardRef
import webbrowser
from io import open
def Leer_Info():
    raiz = Tk
    filename = askopenfilename(filetypes=[("Archivo data","*.data")])
    file = open(filename,"r",encoding = "utf-8")
    texto = file.read()
    return texto

def Leer_Intrucciones():
    raiz1 = Tk
    filename1 = askopenfilename(filetypes=[("Archivo lfp","*.lfp")])
    file1 = open(filename1,"r",encoding = "utf-8")
    texto1 = file1.read()
    return texto1

def Menu():
    print("MENU ANALIZADOR")
    print("--- Seleccione una opcion ---")
    print('1. Cargar Data')
    print('2. Cargar Intrucciones')
    print('3. Analizar')
    print('4. Obtener Grafica')
    print('5. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida