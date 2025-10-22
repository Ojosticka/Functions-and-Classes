

try:
    f = open('test.txt')
    # var = bad_var
    # if f.name == "test.txt":
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")