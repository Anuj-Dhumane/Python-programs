# print(int("10"))
# a = "1000"
# print(int(a))

# b = float("12")
# print(b)

# a = 10
# b = 10
# print(id(a))
# print(id(b))
# print(a is b)
# print(a == b)
# x = 1
# b = sys.getsizeof(x)
# print(b)


# x = [10, 20, 30, 40]
# b = bytes(x)
# print(type(b))
# print(b[0])
# print(b[-1])
# for i in b:
#     print(i)

x = [10, 256]
b = bytearray(x)
for i in b:
    print(i)
