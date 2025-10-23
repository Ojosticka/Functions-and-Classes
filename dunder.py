# # Dunder/Magic Methods

# class Counter:
#     def __init__(self):
#         self.value = 1

#     def count_up(self):
#         self.value += 1
#         return self.value
    
#     def count_down(self):
#         self.value -= 1

#     def __str__(self):
#         return f"Count={self.value}"
    
#     def __add__(self, other):
#         if isinstance(other, Counter):
#             return self.value + other.value
#         raise Exception("Invalid type")


# count1 = Counter()
# count2 = Counter()

# count1.count_up()
# count2.count_up()

# print(count1, count2)
# print(count1 + 2)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    # __str__ is meant for a user friendly output, printing on a class by default would look for this method
    def __str__(self):
        return f"This car is an {self.make} {self.model}, {self.year}"

    # __repr__ is meant for a more detailed, unambiguous output
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"
    
car1 = Car("Hyundai", "L45", 2024)

print(car1.__str__())
print(car1.__repr__())
    






















