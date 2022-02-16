from enum import Enum

class TypeTokenVentas(Enum):
    MES=1
    AÑO = 2
    PRODUCTO = 3
    PRECIO = 4
    CANTIDAD = 5
    DOS_PUNTOS = 6
    IGUAL = 7
    PARENTESIS_ABRE = 8
    CORCHETE_ABRE = 9
    COMA = 10
    CORCHETE_CIERRA = 11
    PUNTO_COMA = 12
    PARENTESIS_CIERRA = 13
    DESCONOCIDO = 14
    LETRAS = 15
    NUMEROS = 16
    ENTERO = 17
    DECIMAL = 18
    
