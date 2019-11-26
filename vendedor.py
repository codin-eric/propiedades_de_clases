""""Mis vendedores"""


class DescuentoError(Exception):
    """Excepcion por descuento"""

    def __init__(self, msj):
        self.msj = msj


class Vendedor:
    """Clase para calcular las ventas"""

    dolar = 60

    def calcular_venta_normal(self, precio):
        """Calcular venta normal"""
        return self.dolar * precio

    def calcular_venta_promocion(self, precio, descuento):
        """Calcular venta con promocion
        el descuento debe ser un float entre 0.1 y 0.90
        """
        if descuento > 0.90 or descuento < 0.1:
            raise DescuentoError(f"El descuento pasado es incorrecto {descuento}")
        return self.dolar * precio * descuento


if __name__ == "__main__":
    venta1 = Vendedor()
    precio = venta1.calcular_venta_normal(20)
    print(precio)

    venta2 = Vendedor()
    precio = venta2.calcular_venta_promocion(20, 0.5)
    print(precio)

    Vendedor.dolar = 65
    venta1 = Vendedor()
    precio = venta1.calcular_venta_normal(20)
    print(precio)

    venta2 = Vendedor()
    precio = venta2.calcular_venta_promocion(20, 0.5)
    print(precio)
