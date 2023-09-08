# num = int(input("Enter the number to print star pattern:"))
# for i in range(num, 0, -1):
#     for j in range(i):
#         if i > 0 and j > 0:
#             print(" ")

#         print("*", end=" ")
#     print("\n")

num = int(input("Enter the number to print star pattern:"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=' ')
    print("\n")
