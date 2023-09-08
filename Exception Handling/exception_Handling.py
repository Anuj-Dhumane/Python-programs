try:
    print(10/0)
except ZeroDivisionError as a:
    print("the description of exception", a)
    print("the id of exception", id(a))
    print("the type exception", type(a))
    print("the type exception", a.__class__)
    print("the name of exception", a.__class__.__name__)
