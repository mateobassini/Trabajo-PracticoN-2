from Ejercicio1 import MaestroPizzero
from Ejercicio3 import Mozo

class TesterPizzeria:
     def main(self):
        # Crear los objetos de tipo MaestroPizzero, Mozo y Pizza
        maestro = MaestroPizzero()
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