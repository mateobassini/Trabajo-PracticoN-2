
# 1. Clase MaestroPizzero

class MaestroPizzero:
    # Constructor
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []

    # Comandos
    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPedido(self, var: str):
        if var:  # Requiere que var no sea vacío
            pizza = Pizza(var)
            self.pizzasPorCocinar.append(pizza)
        else:
            print("Error: La variedad de pizza no puede estar vacía")

    def cocinar(self):
        if self.pizzasPorCocinar:
            self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
            self.pizzasPorCocinar.clear()  # Limpiar la lista de pizzas por cocinar

    def entregar(self, pizzas: int):
        # Retorna hasta un máximo de 2 pizzas para entregar
        a_entregar = self.pizzasPorEntregar[:pizzas]  # Tomar hasta 'pizzas' elementos
        self.pizzasPorEntregar = self.pizzasPorEntregar[pizzas:]  # Remover las pizzas entregadas
        return a_entregar

    # Consultas
    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar
    
    
    # 2. Clase Pizza
    
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


# 3. Clase Mozo

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
    
    
    
    # 5. Clase TesterPizzeria
    
    class TesterPizzeria:
    def main(self):
        # Crear los objetos de tipo MaestroPizzero, Mozo y Pizza
        maestro = MaestroPizzero("Juan")
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Roberto")

        # MaestroPizzero toma pedidos
        maestro.tomarPedido("Muzzarella")
        maestro.tomarPedido("Napolitana")
        maestro.tomarPedido("Calabresa")

        # Cocinar las pizzas
        maestro.cocinar()

        # Entregar hasta 2 pizzas
        pizzas_para_entregar = maestro.entregar(2)

        # Los mozos toman las pizzas
        mozo1.tomarPizzas(pizzas_para_entregar)

        # Entregar las restantes
        pizzas_para_entregar = maestro.entregar(2)

        # Los mozos toman las pizzas restantes
        mozo2.tomarPizzas(pizzas_para_entregar)

        # Servir las pizzas
        mozo1.servirPizzas()
        mozo2.servirPizzas()


if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
    
    
    
    
    
    
    
    
    
    
    



