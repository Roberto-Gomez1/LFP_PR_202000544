import matplotlib.pyplot as plt
from LexicoVentas import LexicoVentas 
from LexicoInstrucciones import LexicoInstrucciones

class Graficadora():
    def __init__(self):
        self.ayuda = []
    
    def general():
        aux = LexicoInstrucciones.tipog[0]
        print(aux)
        if aux == "PIE":
            Graficadora.g_pie()
        #elif aux == "BARRAS":
        #elif aux == "LINEAS":

    def g_pie():
        fig,ax =plt.subplots()
        g = ax.pie(
            LexicoVentas.lista_c,
            labels = LexicoVentas.lista,
            shadow = True,
            autopct= '%1.1f%%'
            )
        plt.show()

