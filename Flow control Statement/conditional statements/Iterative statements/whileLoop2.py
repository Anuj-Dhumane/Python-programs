# # To display the sum of first n numbers
n = int(input("Enter number:"))
sum = 0
i = 1
while i <= n:
    sum = sum+i
    i = i+1
    print("The sum of first", n, "numbers is :", sum)

# write a program to prompt user to enter some name until entering Durga
name = ""
while name != "durga":
    name = input("Enter Name:")
    print("Thanks for confirmation")
