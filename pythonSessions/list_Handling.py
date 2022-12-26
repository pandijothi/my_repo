ls1=[23,34,5,22]
print(ls1)

ls1.append(500)
print(ls1)

ls1.insert(2,34) #2 is the index value.. if you want to insert the string in particular index
print(ls1)

ls2=["Jothi","Riya","Hary"]
ls1.extend(ls2)
print(ls1)

ls3=[8,7,5]
print(ls1+ls3)

print(ls1.pop())
print(ls1)

print(ls1.pop(2))
print(ls1)

print(ls1.remove("Jothi"))
print(ls1)

del ls1[1]
print(ls1)

# ls1.clear()
# print(ls1)
ls1.pop()
ls1.sort()
print(ls1)

ls1.sort(reverse = True)
print(ls1)

ls1.reverse()
print(ls1)

print(ls1.index(5))

print(ls1.count(5))

ls4=ls1.copy()
print(ls4)

