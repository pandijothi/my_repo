import time, calendar
print(time.time())

print(time.ctime())

print(calendar.month(2023,1))

try:
    a=int(input("Enter Integer number:"))
    b=a/0
    print("Output value:",b)
except ZeroDivisionError:
    print("Division Error")
else:
    print('correct value')
finally:
    print('Program ended')
