import threading

class ConfiguracionSingleton:
    
    _instancia = None
    _lock = threading.Lock() 
    _inicializado = False

    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        
        with self._lock:
            if self._inicializado:
                return
            
            self.modo = "Producción"
            self.idioma = "es-CO"
            self.modo_debug = False
            print("SINGLETON: Instancia de Configuración Creada e Inicializada.")
            self._inicializado = True

    def mostrar_config(self):
        print(f"Configuración [Modo: {self.modo}, Idioma: {self.idioma}, Debug: {self.modo_debug}]")