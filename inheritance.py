##def add(a,b):
##    print(a+b)
##add(1,2)

##def add(a,b):
##    return a+b
##print(add(1,2))

##def fun(a):
##    if a%2==0:
##        print('hello')
##    else:
##        print('bye')
##print(fun(1))
##fun(2)
##fun(3)
##
##def fun1(a):
##    if a%2==0:
##        return 'hello'
##    else:
##        return 'bye'
##print(fun1(1))

##a=10
##print(a)
##def add():
##    a=20
##    print(a)
##    def inn():
##        nonlocal a
##        a=11
##        print(a)
##    inn()
##    print(a)
##add()
##print(a)


##def add(a,b):
##    print(f'{a}+{b}={a+b}')
##add(4,3)#positionall argunment


##def add(a,b):
##    print(f'{a}+{b}={a+b}')
##add(5,3)
##add(b=3,a=4)#keyword argunment
##

##def add(a,b,c,d,e):
##    print(a,b,c,d,e)
##add(4,5,6,d=2,e=5)
##add(4,b=5,6,d=2,e=5)
##add(a=1,2)


##def add(a,b,c,d,e,f,/):
##    print(a,b,c,d,e,f)
##add(1,2,3,4,5,6)
##add(1,2,3,4,5,f=6)
##add(a=1,b=2,c=3,d=5,e=4,f=6)


##def add(*,a,b,c,d,e,f):
##    print(a,b,c,d,e,f)
##add(a=1,b=2,c=3,d=4,e=5,f=6)
##add(1,2,3,4,5,6)


##def add(a,b,c,/,*,d,e,f):
##    print(a,b,c,d,e,f)
##add(1,2,3,d=4,e=5,f=6)
##add(1,2,3,4,5,6)

##n=5
##fact=1
##while n>0:
##    fact=fact*n
##    n-=1
##print(fact)

##def factorial(n):
##    if n == 1:  #5==1 false, 4==1 false
##        return 1
##    else:
##        return n*factorial(n-1) #5*4*fact(3)
##print(factorial(5))

##n=4
##def sq(n):
##    return n**2
##print(sq(n))
##n=4
##a=lambda n:n**2
##print(a(n))

##def fun(i):
##    return len(str(i))
##print(fun(100))
##
##a=lambda i:len(str(i))
##print(a(100))


##def upper(i):
##    return i.upper()
##print(upper("hello"))
##
##a= lambda i:i.upper()
##print(a("hello"))


##l=['a','b','c','d']
##d={}
##def fun(l):
##    for i,j in enumerate(l):
##        d[i]=j
##fun(l)
##print(d)
##
##a= lambda l: dict(enumerate(l))
##print(a(l))

####normal function without map
##l=[1,2,3,4,5,6,7,8,9,10]
##l1=[]
##def fun(l):
##    for i in l:
##        l1.append(i**2)
##fun(l)
##print(l1)
##
####normal function with map
##l=[1,2,3,4,5,6,7,8,9,10]
##def fun(l):
##    return l**2
##print(list(map(fun,l)))
##
###anonymous function
##
##l=[1,2,3,4,5,6,7,8,9,10]
##fun = lambda a:a**2
##print(list(map(fun,l)))
##
###single line expression
##
##print(list(map(lambda a:a**2,l)))


####normal function without filter
##l=[1,2,3,4,5,6,7,8,9,10]
##l1=[]
##def fun(l):
##    for i in l:
##        if i%2==0:
##            l1.append(i)
##fun(l)
##print(l1)
##
##
####normal function with filter
##l=[1,2,3,4,5,6,7,8,9,10]
##def fun(l):
##    return l%2==0
##print(list(filter(fun,l)))
##
##
###anonymous function
##
##l=[1,2,3,4,5,6,7,8,9,10]
##fun = lambda a:a%2==0
##print(list(filter(fun,l)))
##
##
###single line expression
##
##print(list(filter(lambda a:a%2==0,l)))


##def outer(x):
##    def inner(y):
##        return x + y
##    return inner
##
##add=outer(5)
##print(add(10))

##
##def outer(func):#1#4
##    def inner(a,b):#5#8
##        print("hello decorator output is:",end=' ')#9
##        func(a,b)#add(4,3)#10
##    return inner#6
##@outer#add=outer(add)#3
##def add(a,b):#2#11
##    print(a+b)#12
##add(4,3)#7



##def outer(func):
##    def inner(*args,**kwargs):
##        print("you got output:",end=' ')
##        func(*args,**kwargs)
##    return inner
##@outer
##def add(*args,**kwargs):
##    print(f"args:{args},kwargs:{kwargs}")
##add(1,2,4,5,6,8,a=6,b=7,c=8,d=9)


##from time import sleep
##
##def outer(a):
##    def inner(*args,**kwargs):
##        print("the output is :", end=' ')
##        sleep(55)
##        a(*args,**kwargs)
##    return inner
##@outer
##def add(*args,**kwargs):
##    s=0
##    s1=0
##    for i in args:
##        s+=i
##    for j in kwargs.values():
##        s1+=j
##    print(s+s1)
##add(1,2,3,4,5,6,a=7,b=8,c=9,d=10,e=12)
##


##n=[1,2,3,4,5,6,7,8,98,23,57,76]
##i= iter(n)
##
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##print(next(i))
##
##
##
##for i in n:
##    print(i)


##def demo(n):
##    yield n**2
##    yield n**3
##print(list(demo(5)))


##r=(i for i in range(2,101,2))
##print(list(r))



##write a decorator function the given mailid is valid or not #.com has to preaent and @ has to present.


##def outer(func):
##    def inner(mailid):
##        if mailid.endswith(".com") and '@' in mailid:
##            func(mailid)
##        else:
##            print("invalid mailid")
##    return inner
##@outer
##def gmail(mailid):
##    print("mailid is valid for gmail")
##
##@outer   
##def yahoo(mailid):
##    print("mailid is valid for yahoo")
##
##mailid=input("Enter the mailid:")
##
##if 'gmail' in mailid:
##    gmail(mailid)
##elif 'yahoo' in mailid:
##    yahoo(mailid)
##else:
##    print("invalid type of mailid")

##import os
##print(os.getcwd())


import os
print(os.chdir(r"C:\Users\admin\AppData\Local\Programs\Python\Python313"))
print(os.getcwd())    
