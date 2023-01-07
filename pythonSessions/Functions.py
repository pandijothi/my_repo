def func1(name):
    return("welcome",name)


print(func1("Jothi"))

def func3(*args):
    print("Passed Arguments are :", args[0],args[1])


func3('Jothi','Riya')

def func4(**args) :
    print("Arguments :",args['first'],args['second'])

func4(first="Jothi",second="Riya")

import math

print(math.sin(30))

