class Pizza:
    # Constructor
    def __init__(self, var: str):
      self.variedad = var

    # Comandos
    def establecerVariedad(self, var: str):
        self.variedad = var

    # Consultas
    def obtenerVariedad(self):
        return self.variedad