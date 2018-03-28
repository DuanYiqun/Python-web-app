

def ac(x,y,z=6):
    cc=x+y+z
    return cc

d=ac(1,1)
print(d)


d=ac(1,1,z=1)
print(d)

def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,1,1,'good']))
print(add_end())
print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

print(add_end2())
print(add_end2())
print(add_end2())

def calu(*nums):
    sum=0
    for i in nums:
        sum=sum+i*i 
    return sum

print(calu(1,2,2))

nums=[1,2,2]
print(calu(*nums))

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        raise ValueError('there should be no city args')
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('jack','22',salary={'salar':10000},zipcode=0000000,find=True)

#person('jack','22',salary={'salar':10000},zipcode=0000000,find=True,city='test')

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

  
person2('Jack', 24,{'arggg':3},city= 'Beijing', job='Engineer')

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(100))

