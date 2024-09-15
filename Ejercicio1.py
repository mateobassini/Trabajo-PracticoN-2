class MaestroPizzero():
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

    def tomarPedido(self, var):     # paso i)
        if var:
            nueva_pizza = Pizza(var)
            self.pizzasPorCocinar.append(nueva_pizza)

    # Paso ii) Implementar el Comando cocinar
    def cocinar(self):                             
         while self.pizzasPorCocinar:              # Este método mueve todas las pizzas de pizzasPorCocinar 
            pizza = self.pizzasPorCocinar.pop(0)   # a pizzasPorEntregar. 
            self.pizzasPorEntregar.append(pizza)

    # Paso iii): Implementar el Comando entregar
    # retorna hasta un máximo de 2 pizzas de pizzasPorEntregar.

    def entregar(self, cantidad):
        entregadas = []
        for _ in range(min(cantidad, 2)):
            if self.pizzasPorEntregar:
                entregadas.append(self.pizzasPorEntregar.pop(0))
        return entregadas




            
            



                                      
  
        
    


