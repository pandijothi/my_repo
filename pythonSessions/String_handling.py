a="Jothi python classes"

b='''\nPython is the programming language
    and it is a opensource and 
    we can download and use it freely
    with no cost
    '''

print(a,b)

print(len(b))

print(a[1:5]) # 5th place char is exculded. This is called slicing of strings

print(b[len(b)-121])

print(b[6])

for i in a:
    print(i)

print(a.upper())
print(a.lower())
print(a.strip())

print(a.replace("Jothi","Riya"))

stg = "January,February,March,April"
print(stg.split(","))
print(stg.capitalize())

print(stg.center(200,'+')) #if you give two + then it will throw the error

print(stg.count('a'))
print(stg.endswith('l'))
print(stg.index('March'))
print(stg.title())
print(stg.swapcase())
