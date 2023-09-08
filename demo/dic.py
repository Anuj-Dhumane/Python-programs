list2 = ['Anuj', 10, 'Shatyush', 23, 'Nilay', 45]
data = {}
# keys=list2[0]
# for i in range (0,len(list2)):
#     keys2=keys +
keys = list2[0:len(list2):2]
values = list2[1:len(list2):2]
data[keys] = values

print(data)
# print(keys)
# print(value)
