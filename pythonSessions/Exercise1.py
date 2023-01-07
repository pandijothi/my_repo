#3. Print the characters of a string that are present at even indices.
stg="Python"
print("Given String:",stg)
print("output:")
for i in range(len(stg)):
    if i%2==0:
        print(stg[i])

#4.  Check if the first and last number of a list is the same
lst1=[10, 20, 30, 40, 10]
#lst1=[12, 23, 34, 55]
print("Given List",lst1)
print("Check if First and Last number of the list is same\n")
if(lst1[0]==lst1[-1]):
    print("True")
else:
    print("False")

#5. Display numbers divisible by 5 from a list
lst1 = [10, 20, 33, 46, 55]
for i in range(len(lst1)):
    if lst1[i]%5==0:
        print(lst1[i])

#6. Return the count of a given substring from a string
str_x = "Emma is good developer. Emma is a writer"
print("Emma is appeared in", str_x.count("Emma") ,"times")

#7. Print the following pattern
for i in range(1,6):
    #print('\n')
    for j in range(0,i):
        print(i,end='\t')
    print(end='\n')

