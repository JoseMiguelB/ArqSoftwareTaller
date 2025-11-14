import abc
from productos import *

class FabricaElectronicos(abc.ABC):
    
    @abc.abstractmethod
    def crear_computadora(self) -> Computadora:
        pass

    @abc.abstractmethod
    def crear_telefono(self) -> Telefono:
        pass

    @abc.abstractmethod
    def crear_tableta(self) -> Tableta:
        pass

class FabricaPremium(FabricaElectronicos):
    def crear_computadora(self) -> Computadora:
        return ComputadoraPremium()

    def crear_telefono(self) -> Telefono:
        return TelefonoPremium()

    def crear_tableta(self) -> Tableta:
        return TabletaPremium()

class FabricaEstandar(FabricaElectronicos):
    def crear_computadora(self) -> Computadora:
        return ComputadoraEstandar()

    def crear_telefono(self) -> Telefono:
        return TelefonoEstandar()

    def crear_tableta(self) -> Tableta:
        return TabletaEstandar()

class FabricaEconomica(FabricaElectronicos):
    def crear_computadora(self) -> Computadora:
        return ComputadoraEconomica()

    def crear_telefono(self) -> Telefono:
        return TelefonoEconomico()

    def crear_tableta(self) -> Tableta:
        return TabletaEconomica()