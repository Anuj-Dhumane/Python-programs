# Writing data to text file

f = open("D:\demo_file.txt", 'w')
f.write("Anuj\n")
f.write("Mahendrarao\n")
f.write("Dhumane\n")
print("Data written to the file successfully")
f.close()


f = open("abcd.txt", 'w')
list = ["sunny\n", "bunny\n", "vinny\n", "chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()
