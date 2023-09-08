# a = 10
def fun():
    global a
    print(a)


def fun1():
    print(a)


fun()
fun1()
