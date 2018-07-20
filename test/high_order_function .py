from functools import reduce

def add(x, y, f):
    return f(x) + f(y)

def f(temp):
    a=temp*temp+temp
    return a

print(add(5,-5,f))

def fn(x,y):
    return x*10+y

reduce(fn,[1,2,3,34,4])

