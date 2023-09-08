# check if an item exists in the python tuple or not

t = (12, 23, 7, 'z', "Anuj", 37.034)
i = eval(input("Enter the value to check : "))
if i in t:
    print("The tuple t contains ", i)

else:
    print("The tuple t doesn't contains ", i)


my_tuple = (12, 23, 7, 'z', "Anuj", 37.034)

# Check if an item exists in the tuple
if 23 in my_tuple:
    print("Item 3 exists in the tuple")
else:
    print("Item 3 does not exist in the tuple")

if 6 not in my_tuple:
    print("Item 6 does not exist in the tuple")
else:
    print("Item 6 exists in the tuple")
