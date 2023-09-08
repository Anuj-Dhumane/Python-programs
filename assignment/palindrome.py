string1 = eval(input(("Enter a letter:")))
if (string1 == string1[::-1]):
    print("The letter is a palindrome")
else:
    print("The letter is not a palindrome")
