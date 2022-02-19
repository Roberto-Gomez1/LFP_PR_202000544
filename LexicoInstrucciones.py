from Token import Token
from TypeToken import TypeToken


class LexicoInstrucciones():
    
    tipo = TypeToken.DESCONOCIDO

    nombre_grafica = ''
    tipo_grafica = ''
    titulo_grafica=''
    titulox_g=''
    tituloy_g=''

    def __init__(self,entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens= []
        entrada = entrada + "&"
        actual = ''
        longitud = len(entrada)

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
                elif actual == '<':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.MENOR.name)
                    continue
                elif actual == '>':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.MAYOR.name)
                    continue
                elif actual == '¿':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.INTERRO_ABRE.name)
                    continue
                elif actual == '?':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.INTERRO_CIERRA.name)
                    continue
                elif actual == ',':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.COMA.name)
                    continue
                elif actual == ':':
                    self.lexema += actual
                    self.AgregarToken(TypeToken.DOS_PUNTOS.name)
                    continue
                elif actual =='&':
                    print( 'ANALISIS INSTRUCCIONES TERMINADO')
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
                        i -= 1
                        continue
                    else:
                        self.AgregarToken(TypeToken.LETRAS.name)
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
                    self.AgregarToken(TypeToken.MENSAJE.name)


    def AgregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo))
        self.lexema =''
        self.estado = 0
        self.tipo = TypeToken.DESCONOCIDO

    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['NOMBRE', 'GRAFICA', 'TITULO', 'TITULOX', 'TITUTLOY']
        if palabra =='NOMBRE':
            self.tipo = TypeToken.NOMBRE  
            return True
        if palabra == 'GRAFICA':
            self.tipo = TypeToken.GRAFICA 
            return True
        if palabra == 'TITULO':
            self.tipo = TypeToken.TITULO 
            return True
        if palabra == 'TITULOX':
            self.tipo = TypeToken.TITULO_X 
            return True
        if palabra == 'TITULOY':
            self.tipo = TypeToken.TITULO_Y 
            return True
        return False

    def printTokens(self):
        for token in self.tokens:
            print(token.lexema + " -> Tipo: " + str(token.type))
    
    aux_tipoG= ''
    aux_nombreG= ''
    aux_titulo= ''
    aux_titulox= ''
    aux_tituloy= ''
    tipog= []
    tipon= []
    tipotit= []
    tipotitx= []
    tipotity = []

    def GuardarDatos(self):
        longitud = len(self.tokens)
        for i in range(longitud):
            if self.tokens[i].type == TypeToken.NOMBRE.name:
                i = i + 1
                if self.tokens[i].lexema == ":":
                    self.nombre_grafica = self.tokens[i+1].lexema
                else:
                    self.nombre_grafica = self.tokens[i].lexema
            elif self.tokens[i].type == TypeToken.GRAFICA.name:
                i = i + 1
                if self.tokens[i].lexema == ":":
                    self.tipo_grafica = self.tokens[i+1].lexema
                else:
                    self.tipo_grafica = self.tokens[i].lexema
            elif self.tokens[i].type == TypeToken.TITULO.name:
                i = i+1
                if self.tokens[i].lexema == ":":
                    self.titulo_grafica = self.tokens[i+1].lexema
                else:
                    self.titulo_grafica = self.tokens[i].lexema
            elif self.tokens[i].type == TypeToken.TITULO_X.name:
                i = i+1
                if self.tokens[i].lexema == ":":
                    self.titulox_g = self.tokens[i+1].lexema
                else:
                    self.titulox_g = self.tokens[i].lexema

            elif self.tokens[i].type == TypeToken.TITULO_Y.name:
                i = i+1
                if self.tokens[i].lexema == ":":
                    self.tituloy_g = self.tokens[i+1].lexema
                else:
                    self.tituloy_g = self.tokens[i].lexema


        a = self.tipo_grafica.replace('"','')
        self.aux_tipoG = a.upper();
        self.tipog.append(self.aux_tipoG)

        b= self.nombre_grafica.replace('"','')
        self.aux_nombreG = b.upper();
        self.tipon.append(self.aux_nombreG)
        #print(self.tipon)

        c = self.titulo_grafica.replace('"','')
        self.aux_titulo = c.upper();
        self.tipotit.append(self.aux_titulo)
        #print(self.tipotit)

        d=self.titulox_g.replace('"','')
        self.aux_titulox = d.upper();
        self.tipotitx.append(self.aux_titulox)
        #print(self.tipotitx)

        e= self.tituloy_g.replace('"','')
        self.aux_tituloy = e.upper();
        self.tipotity.append(self.aux_tituloy)
        #print(self.tipotity)
        