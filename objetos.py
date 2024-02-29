


class Persona:
    #Esto se conoce como el constructor de clase
    def __init__(self, nombre: str, edad: int, pelicula_favorita: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.pelicula_favorita = pelicula_favorita

    def presentarse(self):
        print(f"Buenas, que bonito es saludar y ser saludado, mi nombre es {self.nombre} tengo {self.edad} y mi película favorita es {self.pelicula_favorita}")

santiago = Persona('Santiago', edad=20, pelicula_favorita='La la land')
herney = Persona('Herney', edad = 34, pelicula_favorita='El paseo 7')



class Animal:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    
    def hacer_sonido(self):
        return 'GUAAAUU'

class Gato(Animal):

    def hacer_sonido(self):
        return 'Miaaaauuuu'

gato = Gato('Doraemon')
perro = Perro('Ayudante de Santa')

print(
    f"mi Gato se llama {gato.nombre} y hace {gato.hacer_sonido()}"
)

print(
    f"mi Perro se llama {perro.nombre} y hace {perro.hacer_sonido()}"
)