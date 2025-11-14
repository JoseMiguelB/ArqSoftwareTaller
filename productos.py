import abc
import copy

class ProductoElectronico(abc.ABC):
    
    @abc.abstractmethod
    def mostrar_info(self):
        pass

    @abc.abstractmethod
    def clonar(self):
        """Implementación del patrón Prototype"""
        pass

class Computadora(ProductoElectronico): pass
class Telefono(ProductoElectronico): pass
class Tableta(ProductoElectronico): pass

class ComputadoraPersonalizada(Computadora):
    def __init__(self):
        self.partes = {}

    def agregar_parte(self, nombre, valor):
        self.partes[nombre] = valor

    def mostrar_info(self):
        print("Computadora Personalizada (Builder):")
        for nombre, valor in self.partes.items():
            print(f"  - {nombre}: {valor}")
    
    def clonar(self):
        clon = ComputadoraPersonalizada()
        clon.partes = copy.deepcopy(self.partes)
        return clon
    
class ComputadoraPremium(Computadora):
    def mostrar_info(self):
        print("Computadora Premium: CPU i9, 32GB RAM, SSD 2TB, RTX 4090")

    def clonar(self):
        return copy.deepcopy(self)

class TelefonoPremium(Telefono):
    def mostrar_info(self):
        print("Teléfono Premium: Pantalla OLED 144Hz, Cámara 200MP")
    
    def clonar(self):
        return copy.deepcopy(self)

class TabletaPremium(Tableta):
    def mostrar_info(self):
        print("Tableta Premium: Pantalla Mini-LED, Soporte Lápiz Pro")
    
    def clonar(self):
        return copy.deepcopy(self)

class ComputadoraEstandar(Computadora):
    def mostrar_info(self):
        print("Computadora Estándar: CPU i5, 16GB RAM, SSD 1TB")

    def clonar(self):
        return copy.deepcopy(self)

class TelefonoEstandar(Telefono):
    def mostrar_info(self):
        print("Teléfono Estándar: Pantalla AMOLED 90Hz, Cámara 50MP")
    
    def clonar(self):
        return copy.deepcopy(self)

class TabletaEstandar(Tableta):
    def mostrar_info(self):
        print("Tableta Estándar: Pantalla LCD, Soporte Lápiz Básico")
    
    def clonar(self):
        return copy.deepcopy(self)

class ComputadoraEconomica(Computadora):
    def mostrar_info(self):
        print("Computadora Económica: CPU i3, 8GB RAM, HDD 1TB")

    def clonar(self):
        return copy.deepcopy(self)

class TelefonoEconomico(Telefono):
    def mostrar_info(self):
        print("Teléfono Económico: Pantalla LCD 60Hz, Cámara 12MP")
    
    def clonar(self):
        return copy.deepcopy(self)

class TabletaEconomica(Tableta):
    def mostrar_info(self):
        print("Tableta Económica: Pantalla LCD Básica")
    
    def clonar(self):
        return copy.deepcopy(self)