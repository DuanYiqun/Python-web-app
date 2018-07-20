def findMinAndMax(L):
    temp_max=0
    temp_min=0
    for value in L:
        if value>temp_max:
            temp_max=value
    
    temp_min=temp_max
    for value in L:
         if value<temp_min:
            temp_min=value

    return (temp_min,temp_max)


print(findMinAndMax([1,7]))
print(findMinAndMax([]))
print(findMinAndMax([123,23,4,23,4,5,76,3,1,35,4,643,23,3,4,1,1,1]))


L=[x*x for x in range(1,11)]
print(L)
L=[x*x for x in range(1,11) if x%2==0]
print(L)
L=[m+n for m in 'name' for n in 'string']
print(L)
g=(m+n for m in 'name' for n in 'string')
print(g)
print(next(g))
print(range(1,100))
for i in range(1,len('name')*len('string')):
    print(next(g))

from collections import Iterable
isinstance([], Iterable)
True
isinstance({}, Iterable)
True
isinstance('abc', Iterable)
True
isinstance((x for x in range(10)), Iterable)
True
isinstance(100, Iterable)
False

it=iter([1,2,23,3,24,2,13,123,1])
for value in range(1,len([1,2,23,3,24,2,13,123,1])+1):
    print(next(it))