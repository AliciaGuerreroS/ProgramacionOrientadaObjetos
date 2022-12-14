"""Cree una clase figura, que tenga los siguientes atributos.

Nombre
Área
Coordenada X
Coordenada Y
Escriba sus respectivos getters y setters de área.

Y cree el método mostrar_figura, qué imprima lo siguiente:

La figura se llama "Nombre"
Tiene un área de "Área" m^2
E inicia en las coordenadas ( "X", "Y" )
Luego, cree un objeto con los siguiente datos.

Nombre = Círculo
Área = 30.5
Coordenada X = -1
Coordenada Y = 2
Llame al método mostrar_figura, y luego destruya el objeto."""

# class Figura:

#     def __init__(self, nombre, area, x, y) -> None:
#         self.nombre= nombre
#         self.__area= area
#         self.x= x
#         self.y= y
    
#     def get__area (self):
#         return self.__area

#     def set__area (self, area):
#         self.__area= area

#     def mostrar_figura (self):
#         print(f"La figura se llama {self.nombre}")
#         print(f"Tiene un área de {self.__area} m^2")
#         print(f"E inicia en las coordenadas {self.x},{self.y}")

# mi_figura= Figura("circulo", 30.5, -1, 2)
# mi_figura.mostrar_figura()

"""Cree una clase Automovil con los siguientes atributos.

Marca
Año
Placa
Número de Asientos
Escriba los getters y setter del atributo marca.

Cree dos métodos, mostrar_carro y tipo_carro.

mostrar_carro imprime:

El carro es de marca "Marca" del año "Año"
Y tiene placa número "Placa"
tipo_carro imprime:

Si el número de asientos es mayor a 20, imprimir:

El automóvil es un bus.
Si el número de asientos es mayor a 10, imprimir:

El automóvil es una combi.
Si no, imprimir:

El automóvil es un carro normal
Crear un objeto con los siguientes datos, y llamar a los métodos creados.

Marca = Suzuki
Año = 2010
Placa = ABC-456
Número de Asientos = 4"""

# class Automovil:

#     def __init__(self, marca, tiempo, placa, numero_asientos) -> None:
#         self.__marca= marca
#         self.tiempo= tiempo
#         self.placa= placa
#         self.numero_asientos= numero_asientos

#     def get__marca (self):
#         return self.__marca

#     def set__marca (self, marca):
#         self.__marca = marca

#     def mostrar_carro(self):
#         print(f"El carro es de marca {self.__marca} del año {self.tiempo}")
#         print(f"Y tiene placa número {self.placa}")

#     def tipo_carro(self):
#         if self.numero_asientos > 20:
#             print(f"El atomovil es un bus.")
#         if self.numero_asientos > 10:
#             print(f"El automovil es una combi")
#         else:
#             print(f"El automovil es un carro normal")

# mi_automovil = Automovil("Suzuki", 2010, "ABC-456", 4)
# mi_automovil.mostrar_carro()
# mi_automovil.tipo_carro()

"""Cree una clase Punto con los siguientes atributos: X, Y

Cree el método mostrar_punto, el cual imprime lo siguiente.

El punto está en ( "X", "Y" )
Luego realice la composición con la clase figura creada anteriormente.

Nota:

Utilice el método mostrar_punto dentro de mostrar_figura
Utilice los mismos datos del ejercicio anterior
Cree un objeto Figura y llame a mostrar_figura, luego elimine el objeto."""

# class Figura:

#     def __init__(self, nombre, area, x, y) -> None:
#         self.nombre= nombre
#         self.__area= area
#         self.x= x
#         self.y= y
#         self.punto= Punto(12,5)   ##composicion
    
#     def __del__(self):
#         return None

#     def get__area (self):
#         return self.__area

#     def set__area (self, area):
#         self.__area= area

#     def mostrar_figura (self):
#         print(f"La figura se llama {self.nombre}")
#         print(f"Tiene un área de {self.__area} m^2")
#         print(f"E inicia en las coordenadas {self.x},{self.y}")
#         self.punto.mostrar_punto()

# class Punto:

#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def mostrar_punto(self):
#         print(f"El punto esta en las coordenadas {self.x} y {self.y}")

# mi_figura= Figura("circulo", 30.5, -1, 2)
# mi_figura.mostrar_figura()
