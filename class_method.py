"""Expliquemos metodos de clases"""
from datetime import date


class Persona:
    """Creador de personas"""

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def from_birth_year(cls, nombre, year):
        return cls(nombre, date.today().year - year)

    @staticmethod
    def es_adulto(edad):
        return edad > 18


persona1 = Persona("Pablo", 20)
print(persona1.edad)

persona2 = Persona.from_birth_year("Eric", 1991)
print(persona2.edad)

if Persona.es_adulto(persona2.edad):
    print("Estas viejo")
else:
    print("Estas a la onda")
