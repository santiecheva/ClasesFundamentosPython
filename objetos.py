


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

print(herney.presentarse())