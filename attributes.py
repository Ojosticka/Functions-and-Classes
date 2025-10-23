# class Person:
#     number_of_people = 0    # this is a class attribute

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     @classmethod
#     def number_of_people_(cls):     # they dont reference a class method, they reference the class itself and the class attributes and dont depend on an instance
#         return cls.number_of_people
    
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1


# p1 = Person("tim")
# p2 = Person("jugernut")

# print(Person.number_of_people_())


# Static Methods;

class Math:
    
    @staticmethod    #this means static and not changing
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
    
Math.pr()
