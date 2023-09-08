num = int(input("Enter the number to check whether it is prime or not : "))
for i in range(2, num):
    if (num % i == 0):
        print("Not prime number")
        break
else:
    print("prime number")
