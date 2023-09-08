l = [10, 10, 20, 20, 34, 34]
s = set(l)
p = list(s)
print(p)
print(type(p))

# approach 2nd :
set = [12, 12, 45, 45, 39, 20, 20]
s = []
for i in set:
    if i not in s:
        s.append(i)
print(s)
