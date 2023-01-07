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

#Find the sum of all the numbers in the list

ls1=[34,22,12,23,45]

a=0
for i in ls1:
    a = a +i

print("Sum of all numbers", a)

lst1=[4,6,4,3,5,6]
lst2=["Riya","Jothi"]
lst2.extend(lst1)
print(lst2)
print(lst1+lst2)

days=['Monday','Tuesday','Wednesday','Thursday']
# days.remove("Monday")
#days.index(1)
print(days.sort())
print(days.reverse())

del days[-1]
print(days)

print(lst1.count(4))

lst3=lst1.copy()
print("List3:",lst3)

lst4=lst3
print("List4:",lst4)

for i in lst4:
    print(i**2)

lst6=[i**2 for i in lst4]
print(lst6)
#
# lst3=[i for i in lst6 if i%2==0]
# print(lst3)

print(lst6[-2])

print(lst6[len(lst6)-2])
print(lst6[:])
print(lst6[2:5:2])
print(lst6[::2])
print(lst6[:len(lst6)])
days.clear()


print(days)
