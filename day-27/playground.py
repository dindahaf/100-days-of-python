def add(*args): #Unlimited Arguments
    total = 0
    for n in args:
        total += n
    return total

print(add(5,5,3))

def add2(*args):
    print(args[1])

add2(5,1,3)

def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)

def calculate2(**kwargs):
    print(kwargs)
    print(kwargs["add3"])

def calculate3(n, **kwargs):
    print(kwargs)
    n += kwargs["add5"]
    n *= kwargs["multiply5"]
    print(n)

calculate(add=1, multiply = 3)
calculate2(add3=4, add4=5)
calculate3(1,add5=1, multiply5=3)

