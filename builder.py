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
    
    @abc.abstractmethod
    def set_enfriamiento(self, enfriamiento: str):
        """Nuevo paso abstracto para el enfriamiento"""
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
    
    def set_enfriamiento(self, enfriamiento: str):  
        self._producto.agregar_parte("Enfriamiento", enfriamiento)
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
        print("\nDirector: Construyendo PC Gamer...")
        (self.builder
            .set_cpu("Intel i9-14900K")
            .set_ram("64GB DDR5 6000MHz")
            .set_almacenamiento("4TB NVMe SSD Gen5")
            .set_gpu("NVIDIA RTX 4090")
            .set_fuente_poder("1200W Platinum")
            .set_enfriamiento("Refrigeración Líquida Custom 360mm") 
        )

    def construir_pc_oficina(self):
        print("\nDirector: Construyendo PC de Oficina...")
        (self.builder
            .set_cpu("Intel i5-14400")
            .set_ram("16GB DDR4 3200MHz")
            .set_almacenamiento("1TB NVMe SSD Gen4")
            .set_gpu("Gráficos Integrados Intel")
            .set_fuente_poder("500W Bronze")
            .set_enfriamiento("Disipador de Aire de Stock") 
        )
