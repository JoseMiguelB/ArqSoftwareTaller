import abc
from productos import ComputadoraPersonalizada


class ComputadoraBuilder(abc.ABC):
    
    @property
    @abc.abstractmethod
    def producto(self) -> ComputadoraPersonalizada:
        pass

    @abc.abstractmethod
    def reiniciar(self):
        pass

    @abc.abstractmethod
    def set_cpu(self, cpu: str):
        pass
    
    @abc.abstractmethod
    def set_ram(self, ram: str):
        pass

    @abc.abstractmethod
    def set_almacenamiento(self, almacenamiento: str):
        pass
    
    @abc.abstractmethod
    def set_gpu(self, gpu: str):
        pass

    @abc.abstractmethod
    def set_fuente_poder(self, fuente: str):
        pass

class BuilderPCConcreta(ComputadoraBuilder):
    
    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self._producto = ComputadoraPersonalizada()

    @property
    def producto(self) -> ComputadoraPersonalizada:
        producto_final = self._producto
        self.reiniciar()
        return producto_final

    def set_cpu(self, cpu: str):
        self._producto.agregar_parte("CPU", cpu)
        return self

    def set_ram(self, ram: str):
        self._producto.agregar_parte("RAM", ram)
        return self

    def set_almacenamiento(self, almacenamiento: str):
        self._producto.agregar_parte("Almacenamiento", almacenamiento)
        return self

    def set_gpu(self, gpu: str):
        self._producto.agregar_parte("GPU", gpu)
        return self
    
    def set_fuente_poder(self, fuente: str):
        self._producto.agregar_parte("Fuente de Poder", fuente)
        return self

class Director:
    def __init__(self, builder: ComputadoraBuilder):
        self._builder = builder

    @property
    def builder(self) -> ComputadoraBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ComputadoraBuilder):
        self._builder = builder

    def construir_pc_gamer(self):
        """Construye una PC Gamer de alta gama"""
        print("\nDirector: Construyendo PC Gamer...")
        self.builder.set_cpu("Intel i9-14900K")
        self.builder.set_ram("64GB DDR5 6000MHz")
        self.builder.set_almacenamiento("4TB NVMe SSD Gen5")
        self.builder.set_gpu("NVIDIA RTX 4090")
        self.builder.set_fuente_poder("1200W Platinum")

    def construir_pc_oficina(self):
        """Construye una PC de oficina básica"""
        print("\nDirector: Construyendo PC de Oficina...")
        self.builder.set_cpu("Intel i5-14400")
        self.builder.set_ram("16GB DDR4 3200MHz")
        self.builder.set_almacenamiento("1TB NVMe SSD Gen4")
        self.builder.set_gpu("Gráficos Integrados Intel")
        self.builder.set_fuente_poder("500W Bronze")