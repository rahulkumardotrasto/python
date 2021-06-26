class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def mymethod():
        print("static method called")


Person.mymethod()
p1 = Person("Rahul", 27, "M")
print(p1.Name)

p1.Name = "Kumar"
print(p1.Name)

# Person.mymethod
