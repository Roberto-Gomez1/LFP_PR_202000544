from numpy import double
from Token import Token
from TypeTokenVentas import TypeTokenVentas
from Objetos import  Objeto

class LexicoVentas():
    
    tipo = TypeTokenVentas.DESCONOCIDO

    mes = ''
    año = 0
    cantidad = 0
    producto = ''
    todo = 0
    precio = 0.0
    ayuda =[]
    def __init__(self,entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens= []
        #self.lista = []
        entrada = entrada + "&"
        actual = ''
        actu = ''
        longitud = len(entrada)
        '''for j in range(longitud):
            actu = entrada[j]
            if self.estado == 0:
                if actu == ':':
                    self.lexema += actu
                    self.AgregarToken(TypeTokenVentas.DOS_PUNTOS.name)
                    continue'''

        for i in range(longitud):
            actual = entrada[i]
            if self.estado == 0:

                if actual.isalpha():
                    self.estado = 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 2
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 4
                    self.lexema += actual
                    continue
                elif actual == '=':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.IGUAL.name)
                    continue
                elif actual == '(':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.PARENTESIS_ABRE.name)
                    continue
                elif actual == ')':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.PARENTESIS_CIERRA.name)
                    continue
                elif actual == '[':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.CORCHETE_ABRE.name)
                    continue
                elif actual == ']':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.CORCHETE_CIERRA.name)
                    continue
                elif actual == ',':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.COMA.name)
                    continue
                elif actual == ':':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.DOS_PUNTOS.name)
                    continue
                elif actual == ';':
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.PUNTO_COMA.name)
                    continue
                elif actual =='&':
                    print( 'ANALISIS VENTAS TERMINADO')
                    continue
                elif actual == ' ' or actual =="\n" or actual == "\r" or actual =='\t':
                    self.estado = 0
                    continue
                else:
                    print("@@@@ ERROR: ", actual)
                    self.lexema = ''
                    continue

            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.lexema += actual
                    continue
                else:
                    if self.Reservada():
                        self.AgregarToken(self.tipo.name)
                        #if actual == " ":
                        #    self.estado = 0
                        #elif actual == ":":
                        #    self.estado =7
                        i -= 1
                        continue
                    else:
                        self.AgregarToken(TypeTokenVentas.LETRAS.name)
                        self.estado = 7
                        i -= 1
                        continue
            if self.estado == 2:
                if actual != '"':
                    self.estado = 2
                    self.lexema += actual
                    continue
                else:
                    self.estado = 3
                    self.lexema += actual
                    self.AgregarToken(TypeTokenVentas.PRODUCTO.name)
            if self.estado == 4:
                if actual.isdigit():
                    self.estado = 4
                    self.lexema += actual
                    continue
                elif actual == '.':
                    self.estado = 5
                    self.lexema += actual
                    continue
                else:
                    self.AgregarToken(TypeTokenVentas.ENTERO.name)
                    i -= 1
                    continue
            if self.estado == 5:
                if actual.isdigit():
                    self.estado = 5
                    self.lexema += actual
                    continue
                else:
                    self.AgregarToken(TypeTokenVentas.ENTERO.name)
                    i-= 1
                    continue
            '''if self.estado == 6:
                if actual == ":":
                    self.estado = 6
                    self.lexema += actual 
                    continue
                else:
                    self.estado = 7
                    self.lexema = ''
                    continue
            if self.estado == 7:
                if actual.isdigit():
                    self.estado = 7
                    self.lexema += actual
                    print(actual)
                    continue
                else:  
                    self.AgregarToken(TypeTokenVentas.AÑO.name)
                    i -= 1
                    continue'''


    def AgregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo))
        self.lexema =''
        self.estado = 0
        self.tipo = TypeTokenVentas.DESCONOCIDO

    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['MES']
        if palabra =='ENERO' or palabra =='FEBRERO' or palabra =='MARZO' or palabra =='ABRIL' or palabra =='MAYO' or palabra =='JUNIO' or palabra =='JULIO' or palabra =='AGOSTO' or palabra =='SEPTIEMBRE' or palabra =='OCTUBRE' or palabra =='NOVIEMBRE' or palabra =='DICIEMBRE':
            self.tipo = TypeTokenVentas.MES  
            return True
        return False

    def printTokens(self):
        for token in self.tokens:
            print(token.lexema + " -> Tipo: " + str(token.type))
    
    lista_p = []
    lista_c = []
    lista = []
    lista_total=[]
    lista_año=[]
    lista_mes=[]
    lista_original=[]
    lista_mayor=[]
    lista_menor=[]
    original=[]
    def GuardarDatos(self):
        longitud = len(self.tokens)

        for i in range(longitud):
            if self.tokens[i].type == TypeTokenVentas.MES.name:
                self.mes = self.tokens[i].lexema
                self.lista_mes.append(self.mes)
            elif self.tokens[i].type == TypeTokenVentas.ENTERO.name:
                self.todo = self.tokens[i].lexema
                self.ayuda.append(self.todo)
            elif self.tokens[i].type == TypeTokenVentas.PRODUCTO.name:
                self.producto = self.tokens[i].lexema
                self.lista.append(self.producto)
            #elif 
            #elif self.tokens[i].type == TypeTokenVentas.AÑO.name:
            #    self.año = self.tokens[i].lexema
                #self.tokens.append(Token(self.año, TypeTokenVentas.AÑO.name))
                #self.AgregarToken(TypeTokenVentas.AÑO.name)
        lon = len(self.ayuda)
        for j in range (lon):
            if j== 0:
                '''self.precio = self.ayuda[j]
                self.tokens.append(Token(self.precio, TypeTokenVentas.PRECIO.name))
                self.lista_p.append(self.precio)'''
                self.año = self.ayuda[j]
                self.tokens.append(Token(self.año, TypeTokenVentas.AÑO.name))
                self.lista_año.append(self.año)
            elif (j%2) == 0:
                self.cantidad = self.ayuda[j]
                self.tokens.append(Token(self.cantidad, TypeTokenVentas.PRECIO.name))
                self.lista_c.append(self.cantidad)
            else:
                self.precio = self.ayuda[j]
                self.tokens.append(Token(self.precio,TypeTokenVentas.CANTIDAD.name))
                self.lista_p.append(self.precio)

        a= len(self.lista_c)
        for p in range(a):
            producto = double(self.lista_c[p]) * double(self.lista_p[p])
            self.lista_total.append(producto)
        
        for f in range(a):
            self.lista_original.append(Objeto(self.lista[f],self.lista_p[f],self.lista_c[f],self.lista_total[f]))
            self.original.append(Objeto(self.lista[f],self.lista_p[f],self.lista_c[f],self.lista_total[f]))
            self.lista_mayor.append(Objeto(self.lista[f],self.lista_p[f],int(self.lista_c[f]),self.lista_total[f]))
            self.lista_menor.append(Objeto(self.lista[f],self.lista_p[f],int(self.lista_c[f]),self.lista_total[f]))
        self.lista_original.sort(key=lambda zz:zz.total,reverse=True)
        self.lista_mayor.sort(key=lambda x:x.cantidad,reverse=True)
        self.lista_menor.sort(key=lambda yy:yy.cantidad,reverse=False)
        print(self.lista_original)
        print(self.lista_mayor)
        print(self.lista_menor)
        #print(self.lista_original)
        #print(self.lista_total)
        #print(self.lista_p)
        #print(self.lista)
        #print(self.lista_c)
        #print(self.año)
    
