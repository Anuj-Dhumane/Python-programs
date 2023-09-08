def fib(n):
    a = 0
    b = 1
    c = 0
    while (c <= n):
        print(c)
        c = a+b
        a = b
        b = c


n = int(input("Enter the number : "))
fib(n)
