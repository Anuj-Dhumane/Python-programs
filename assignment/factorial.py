# def factorial(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#     return num


# f = factorial(5)
# print(f)
def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


a = int(input("enter the number : "))
result = fact(a)
print(result)
