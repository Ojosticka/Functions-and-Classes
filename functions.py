# def increment(number, by=1):
#     return number + by 

# #all required parameters must come before all non-required parameters

# print(increment(4))


# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     print(total)

# multiply(2,3,4,5)

# def save_user(**user):
#     print(user["name"])


# save_user(id=1, name="Tobi", age=27)

# def fizz_buzz(input):
#     if input%3 == 0 and input%5 == 0:
#         print("FizzBuzz")
#     elif input%3 == 0:
#         print("Fizz")
#     elif input%5 == 0:
#         print("Buzz")
#     else:
#         print(input)

# fizz_buzz(int(input("Enter a number to test with: ")))


# def student(**kwargs):
#     # print(args)
#     print(kwargs)


# student(name="John", age=56)

# output of *args is basically saying we don't know the number of arguments we want to pass to our parameter, and the result comes as a tuple
# output of **kwargs is saying we have keyword arguments defined in the argument and the result comes as a key:value pair dictionary

# def student_deets(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ["Math", "Art"]
# info = {"name": "Oluwatobi", "age": 27}

# student_deets(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """returns if a year is a leap year"""

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):

    # if not 1 <= month <= 12:
    #     return "invalid month"
    
    if month == 2 and is_leap(year):
        return 29
    

    return month_days[month]


try:
    year = int(input("Enter the year you want to use: "))
    month = int(input("Enter the month you want to use: "))

    if not 1 <= month <= 12:
        print("invalid month")

    else:
        print(days_in_month(year, month))

except:
    print("check your inputs again")






