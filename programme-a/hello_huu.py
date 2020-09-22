"""
=================================================
@Project -> File    ：programme-a -> hello_huu
@IDE                ：PyCharm
@Author             ：Huu
@Date               ：2020/9/23 10:04
@email              ：huu_huu_huu@163.com
==================================================
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import *

'''L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])

print(L[1][1])

print(L[2][2])'''

'''w=input("输入体重：")
h=input("输入身高：")

bim=int(w)/(int(h)**2)

if bim < 18.5:
    print("你的bim是：%f,过轻。" % bim)
elif bim < 25:
    print("你的bim是：%f,正常。" % bim)
elif bim < 28:
    print("你的bim是：%f,过重。" % bim)
elif bim < 32:
    print("你的bim是：%f,肥胖。" % bim)
else:
    print("你的bim是：%f,严重肥胖。" % bim)'''

'''def m_abs(a):
    if not isinstance(a,(int,float)):
        raise TypeError('you entered a bad type!') #方便调试错误的查询；
    if a >=0:
        print(a)
    else:
        print(-a)

print(m_abs('a'))'''

'''def m_ok():
    pass #占位函数，没有实际意义，为后面填充做准备；

m_ok()'''

'''def m_move(x,y,step,angle=0):
    nx=x+step*cos(step)
    ny=y+step*sin(step)
    return nx,ny

print(m_move(0,1,5,30))'''

'''def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError("you entered a wrong type!")

    x1=(-b+sqrt(b**2-4*a*c)/(2*a))
    x2=(-b-sqrt(b**2-4*a*c)/(2*a))

    return x1,x2

print(quadratic(1,3,2))'''

'''def m_end(L=None):
    if L is None:
        L=[]
    L.append("end")
    return L

print(m_end())

print(m_end())'''

'''def m_calc(*nums):
    sum=0
    for number in nums:
        sum=sum+number*number

    return sum

print(m_calc(1,2,3))

nums=[1,2,3]
print(m_calc(*nums))'''

'''def m_person(name,age,**kw):
    if not 'city' in kw:
        print("there is no info about city!")
    
    print(name,age,kw)

print(m_person("huu",18))

print(m_person("huu",18,city="shanghai",job="engineer"))

other={'city':'beijing','job':'engineer'}

print(m_person("huu",18,**other))'''

'''def m_person_limited(name,age,*,city,job):
    print(name,age,city,job)

m_person_limited("huu",18,city="beijing",job="engineer")

def m_person(name,age,*args,city,job):
    print(name,age,args,city,job)

m_person("jack",28,1,2,3,city="shanghai",job="chief")
m_person("jack",30)'''

'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(1000))'''

'''def fact_n(n,res):
    if n==1:
        return res
    return fact_n(n-1,n*res)

print(fact_n(1000,1))'''

def hanoi(n,a,b,c):
    if n==1:
        print(a,"->",c)
    else:
        hanoi(n - 1, a, c, b)
        print(a,"->",c)
        hanoi(n - 1, b, a, c)

hanoi(64,'a','b','c')




