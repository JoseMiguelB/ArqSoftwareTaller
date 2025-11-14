from configuracion_singleton import ConfiguracionSingleton
from factory_method import ComputadoraFactory, TelefonoFactory
from abstract_factory import FabricaPremium, FabricaEconomica, FabricaElectronicos
from productos import ProductoElectronico 
from builder import BuilderPCConcreta, Director

def demo_singleton():
    print("SINGLETON")
    config1 = ConfiguracionSingleton()
    config1.mostrar_config()

    config1.modo_debug = True
    config1.idioma = "en-US"
    
    config2 = ConfiguracionSingleton()
    
    print("Configuración de la 'segunda' instancia:")
    config2.mostrar_config()
    
    print(f"¿config1 es la misma instancia que config2? -> {config1 is config2}")
    print("-" * 25 + "\n")

def demo_factory_method():
    print("FACTORY METHOD")
    fabrica_pc = ComputadoraFactory()
    pc_basico = fabrica_pc.operacion()
    
    fabrica_tel = TelefonoFactory()
    tel_basico = fabrica_tel.operacion()
    print("-" * 25 + "\n")

def crear_familia_completa(fabrica: FabricaElectronicos):
    pc = fabrica.crear_computadora()
    tel = fabrica.crear_telefono()
    tab = fabrica.crear_tableta()
    
    pc.mostrar_info()
    tel.mostrar_info()
    tab.mostrar_info()
    
    return pc 

def demo_abstract_factory():
    print("ABSTRACT FACTORy")
    
    print("Creando familia de productos PREMIUM:")
    fabrica_premium = FabricaPremium()
    pc_premium = crear_familia_completa(fabrica_premium) 
    
    print("\nCreando familia de productos ECONÓMICA:")
    fabrica_economica = FabricaEconomica()
    crear_familia_completa(fabrica_economica)
    
    print("-" * 25 + "\n")
    return pc_premium 

def demo_prototype(producto_a_clonar: ProductoElectronico):
    print("PROTOTYPE")
    print("Producto Original:")
    producto_a_clonar.mostrar_info()
    
    clon = producto_a_clonar.clonar()
    
    print("\nProducto Clonado:")
    clon.mostrar_info()
    
    print(f"\n¿Producto original es el mismo que el clon? -> {producto_a_clonar is clon}")
    print("-" * 25 + "\n")


def demo_builder():
    print("BUILDER") 
    
    builder = BuilderPCConcreta()
    director = Director(builder)
    director.construir_pc_gamer()
    pc_gamer = builder.producto
    pc_gamer.mostrar_info()

    director.construir_pc_oficina()
    pc_oficina = builder.producto
    pc_oficina.mostrar_info()
    
    print("\nConstrucción manual de PC personalizada (Workstation):")
    
    pc_workstation = (builder
        .set_cpu("AMD Threadripper 7980X")
        .set_ram("256GB DDR5 ECC")
        .set_almacenamiento("2x 8TB NVMe SSD Gen5 RAID 0")
        .set_gpu("NVIDIA RTX 6000 Ada")
        .set_fuente_poder("2000W Titanium")
        .set_enfriamiento("Doble Loop Refrigeración Líquida Custom")
        .producto)
    
    pc_workstation.mostrar_info()
    print("-" * 25 + "\n")


if __name__ == "__main__":
    demo_singleton()
    demo_factory_method()
    producto_original = demo_abstract_factory()
    demo_prototype(producto_original)
    demo_builder()
