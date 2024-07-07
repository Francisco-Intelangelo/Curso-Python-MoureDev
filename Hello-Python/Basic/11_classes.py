# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"): # Constructor __init__, alias tiene un valor por defecto
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada, no se puede modificar sin un setter

    def get_name(self): # Especie de getter al llamar la funcion devuelve el name 
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person2 = Person("Héctor", "de Leon", "El loco de los perros")
print(my_other_person2.full_name)
my_other_person2.walk()

my_other_person.full_name = 666
print(my_other_person.full_name)
