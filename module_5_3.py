
    class House:

        def __init__(self, name, number_of_floors):
            self.name = name
            self.number_of_floors = number_of_floors

        def __str__(self):  # должен возвращать строку
            return f'Название: {self.name} Количество этажей: {self.number_of_floors}'

        def __eq__(self, other):
            return self.number_of_floors == other.number_of_floors
        def __lt__(self, other):
            return self.number_of_floors < other.number_of_floors

        def __le__(self, other):
            return self.number_of_floors <= other.number_of_floors

        def __gt__(self, other):
            return self.number_of_floors > other.number_of_floors

        def __ge__(self, other):
            return self.number_of_floors >= other.number_of_floors

        def __ne__(self, other):
            return self.number_of_floors != other.number_of_floors

        def __add__(self, value):
            return self.number_of_floors + value




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
