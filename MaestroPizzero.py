# diagrama

class maestro_pizzero():
    def _init_(self, nombre):
        self.nombre = nombre
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntrega

# Paso i)
# Implementar el Comando tomarPedido 
# Este método crea un nuevo objeto de la clase Pizza 
# y lo agrega a la lista pizzasPorCocinar.