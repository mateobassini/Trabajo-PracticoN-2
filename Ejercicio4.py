from Ejercicio3 import Mozo

mozo1 = Mozo("Alfredo")
mozo2 = Mozo("Alfredo") 

# Respuestas: 

# i.  No, aunque mozo1 y mozo2 tienen el mismo nombre ("alfredo") 
#     como valor para el atributo nombre, no hacen referencia al 
#     mismo objeto. Ambos son instancias diferentes de la clase Mozo,
#     creadas por separado. 

# ii. No, mozo1 y mozo2 no son objetos equivalentes en este caso. 

#     Dos objetos se consideran equivalentes si todos sus atributos 
#     tienen los mismos valores. En este ejemplo, ambos mozos tienen 
#     el mismo valor para el atributo nombre ("alfredo"), pero el atributo pizzas cambia en cada uno: 
#     mozo1 lleva las pizzas de tipo "Muzzarella" y "Napolitana". 
#     mozo2 lleva la pizza de tipo "Calabresa". 
#     Esto hace que no sean equivalentes, ya que tienen valores distintos 
#     en sus atributos (especialmente en la lista de pizzas que cargan). 

# iii. No, los objetos ligados a mozo1 y mozo2 no comparten la misma 
#      posición de memoria. Cada vez que se crea una nueva instancia de la 
#      clase Mozo, se asigna un espacio de memoria diferente. 