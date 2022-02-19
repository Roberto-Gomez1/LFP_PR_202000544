import matplotlib.pyplot as plt
from numpy import obj2sctype
from LexicoVentas import LexicoVentas 
from LexicoInstrucciones import LexicoInstrucciones

class Graficadora():
    def __init__(self):
        self.ayuda = []
    
    def general():
        aux = LexicoInstrucciones.tipog[0]
        aux1 = LexicoInstrucciones.tipon[0]
        aux2 = LexicoInstrucciones.tipotit[0]
        aux3 = LexicoInstrucciones.tipotitx[0]
        aux4 = LexicoInstrucciones.tipotity[0]
        auxaño = LexicoVentas.lista_mes[0]
        auxmes = LexicoVentas.lista_año[0]
        if aux2 == '':
            aux2 =  auxmes + ' - ' + auxaño
        if aux == "PIE" and aux1 != "":
            Graficadora.g_pie(aux2,aux1)
        elif aux == "BARRAS"and aux1 != "":
            Graficadora.g_barra(aux2,aux1,aux3,aux4)
        elif aux == "LINEAS"and aux1 != "":
            Graficadora.g_linea(aux2,aux1,aux3,aux4)
        elif aux == "" or aux1 == "":
            print("No tiene Instrucciones para la grafica")
        else: 
            print("Ocurrio un error, siga el orden del menu")
    def g_pie(aux,aux1):
        fig,ax =plt.subplots()
        g = ax.pie(
            LexicoVentas.lista_total,
            labels = LexicoVentas.lista,
            shadow = True,
            autopct= '%1.1f%%'
            )
        plt.title(aux)
        plt.savefig(aux1)
        plt.show()

    def g_barra(aux,aux1,aux2,aux3):
        fig,ax =plt.subplots()
        g = ax.bar(LexicoVentas.lista, LexicoVentas.lista_total)
        plt.title(aux)
        plt.xlabel(aux2)
        plt.ylabel(aux3)
        plt.savefig(aux1)
        plt.show()

    def g_linea(aux,aux1,aux2,aux3):
        fig,ax =plt.subplots()
        g = ax.plot(LexicoVentas.lista, LexicoVentas.lista_total)
        plt.title(aux)
        plt.xlabel(aux2)
        plt.ylabel(aux3)
        plt.savefig(aux1)
        plt.show()
