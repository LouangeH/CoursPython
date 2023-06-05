from classes.student import showMessage,Print
import platform

if __name__ == '__main__':

    showMessage()
    print('-------------------Printing-------------------')
    Print()

    """
    une classe en python se commence par une lettre maj et doit etre au singular
    """

    """class Person:
        def __init__(self, nom, prenom, age):
            self.nom = nom
            self.prenom = prenom
            self.age = age
        
        def __str__(self) -> str:
            return f"{self.nom}({self.age})"
        
        def showPerson(self):
            print(self.nom, self.age)

    print("-------------------Affichage de la classe mere-------------------")
    p = Person("Hunter","Ishimwe", 23)

    print(p.prenom)

    print("-------------------Affichage de la classe fille-------------------")

    class Student(Person):
        def __init__(self, nom, prenom, age, adress):
            self.nom = nom
            self.prenom = prenom
            self.age = age
            self.adress = adress
            #super().__init__(nom, prenom, age)
        pass

    s = Student("Louange","Hunter", 20, "Kanyosha")
    print(s.adress)
    #s.showPerson()
    # les collections
    """
    """
    1. les listes []
    2. les tuples ()
    3. les sets {}
    4. les dictionnaires {}
    """
    """
    # Dictionnaires

    student={
        'nom': 'Harubuntu',
        'prenom': 'Loua',
        'adress': 'BujaM'
    }

    print(type(student))

    # Liste
    fruits = [
        'Mangue',
        'Banane',
        'Avocat',
        ''
    ]
    print(len(fruits))

    print("-----------------------Affichage avant insert d'un nouveau fruit-----------------------")

    for f in fruits:
        print(f)

    fruits.insert(1,'Pasteque')
    #fruits.append('Pasteque')
    print("-----------------------Affichage apres insert d'un nouveau fruit-----------------------")

    for f in fruits:
        print(f)

    print("------------------------------------------FIN------------------------------------------")

    # uplets

    fruit = ()
    """

    """student={
            'nom': 'Harubuntu',
            'prenom': 'Loua',
            'adress': 'BujaM',
            'tel':'23456789',
            'mail':'harubuntuloua@gmail.com'
        }
    
    print("----------------------------------Affichage des cles----------------------------------")
    for s in student.keys():
        print(s)
    print("---------------------------------Affichage des valeurs---------------------------------")
    for v in student.values():
        print(v)
    print("-------------------------------Affichage des cles/valeurs-------------------------------")
    for k,v in student.items():
        print(f"{k}:{v}")

    print("------------------------------------------FIN------------------------------------------")"""