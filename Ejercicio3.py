class Mozo:
    # Constructor
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []  # Inicializada como lista vacía

    # Comandos
    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPizzas(self, pizzas):
        if len(self.pizzas) + len(pizzas) <= 2:
            self.pizzas.extend(pizzas)  # Agregar las pizzas a la lista
        else:
            print("El mozo no puede tomar más de 2 pizzas a la vez.")

    def servirPizzas(self):
        self.pizzas.clear()  # Limpiar la lista de pizzas

    # Consultas
    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self):
        return len(self.pizzas) < 2