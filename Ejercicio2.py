class Pizza:
    def _init_(self, variedad):
        self.variedad = variedad

    def establecerVariedad(self, variedad):
        self.variedad = variedad

    def obtenerVariedad(self):
        return self.variedad