class Objeto:

    def __init__(self,producto, precio, cantidad,total):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.total = total

    def __repr__(self):
        return f'\nProducto {self.producto} precio {self.precio} cantidad {self.cantidad} total {self.total}'

class ObjetoTabla:
    def __init__(self,producto, total):
        self.producto = producto
        self.total = total

    def __repr__(self):
        return f'\nProducto {self.producto} total {self.total}'