import abc

from productos import (
    ProductoElectronico, ComputadoraEstandar, 
    TelefonoEstandar, TabletaEstandar
)

class ProductoFactory(abc.ABC):
    
    @abc.abstractmethod
    def crear_producto(self) -> ProductoElectronico:
        pass

    def operacion(self):
        producto = self.crear_producto()
        print("Factory Method: Creado producto básico:")
        producto.mostrar_info()
        return producto

class ComputadoraFactory(ProductoFactory):
    def crear_producto(self) -> ProductoElectronico:
        return ComputadoraEstandar()

class TelefonoFactory(ProductoFactory):
    def crear_producto(self) -> ProductoElectronico:
        return TelefonoEstandar()

class TabletaFactory(ProductoFactory):
    def crear_producto(self) -> ProductoElectronico:
        return TabletaEstandar()