class Pizza:
    def __init__(self, tipo: str):
        self.tipo = tipo  # Tipo de pizza (muzzarella, napolitana, etc.)

class Mozo:
    def __init__(self, nom: str):
        self.nombre = nom
        self.pizzas = []

    def establecerNombre(self, nom: str):
        self.nombre = nom

    def tomarPizzas(self, pizzas):
        if len(self.pizzas) + len(pizzas) <= 2:
            self.pizzas.extend(pizzas)
        else:
            raise ValueError("Un mozo no puede llevar más de 2 pizzas.")

    def servirPizzas(self):
        self.pizzas = []

    def obtenerNombre(self) -> str:
        return self.nombre

    def obtenerPizzas(self):
        return self.pizzas

    def obtenerEstadoLibre(self) -> bool:
        return len(self.pizzas) < 2

class Pedido:
    def __init__(self, pizzas: list[Pizza]):
        self.pizzas = pizzas  # Lista de pizzas en el pedido

    def obtenerCantidadPizzas(self) -> int:
        return len(self.pizzas)

class MaestroPizzero:
    def __init__(self):
        self.pedido_actual = None

    def recibirPedido(self, pedido: Pedido):
        if self.pedido_actual is None:
            self.pedido_actual = pedido
            print(f"Preparando {pedido.obtenerCantidadPizzas()} pizzas")
        else:
            print("El maestro pizzero está ocupado con otro pedido.")

    def terminarPedido(self):
        print("Pedido terminado.")
        self.pedido_actual = None

if __name__ == "__main__":
    pizza1 = Pizza("Muzzarella")
    pizza2 = Pizza("Napolitana")
    pizza3 = Pizza("Calabresa")

    pedido = Pedido([pizza1, pizza2, pizza3])

    maestro_pizzero = MaestroPizzero()

    maestro_pizzero.recibirPedido(pedido)

    mozo1 = Mozo("alfredo")
    mozo2 = Mozo("alfredo")

    mozo1.tomarPizzas([pizza1, pizza2])
    print(f"{mozo1.obtenerNombre()} está llevando: {[pizza.tipo for pizza in mozo1.obtenerPizzas()]}")
    mozo1.servirPizzas()

    mozo2.tomarPizzas([pizza3])
    print(f"{mozo2.obtenerNombre()} está llevando: {[pizza.tipo for pizza in mozo2.obtenerPizzas()]}")
    mozo2.servirPizzas()

    maestro_pizzero.terminarPedido()
