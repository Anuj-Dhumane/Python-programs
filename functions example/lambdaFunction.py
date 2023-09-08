# def s(n): return n*n


# print("the square of {n} is {s(2)}")
# print(s(4))

def outer():
    print("outer function started")

    def inner():
        print("inner function execution")
    print("outer function calling inner function")

    inner()


outer()
