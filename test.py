# -*- Coding:utf-8 -*-
def fib(x):
    """Do nothing, but document it.
    fibonacci 实现
       No, really, it doesn't do anything.
    """
    a,b=1,1
    print(a,b,end=' ')
    while b<x:
        a=a+b
        b=a+b
        print(a,b,end=' ')
    print()

fib(100)
print(fib.__doc__)
ia=1
sb='hello world'
c=[1,2,3,4,5]
c.append(6)

for i in range(len(c)):
    if c[i]>4:
        print(c[i])
        break

print(ia,sb,c,len(c),c[2:3])
