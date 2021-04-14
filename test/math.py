#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

#绝对值 abs
print(abs(-20)) #20
print(abs(12.25)) #12.25
#max()可以接受任意多个参数并返回最大的那个
print(max(2,3,-4,5))

#定义空函数
def nop():
  pass

def move(x,y,step,angle):
  nx=x+step*math.cos(angle)
  ny=y+step*math.sin(angle)
  return nx,ny #返回值其实是一个tuple
x,y=move(100,100,60,math.pi/6) #角度转弧度 π是180°
print(x,y)

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解 求平方根函数math.sqrt()
def quadratic(a,b,c):
  d=b*b-4*a*c
  if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    return x1,x2
  elif d==0:
    x1=-b/2*a
    return x1
  else:
    return "无解"
#测试函数
print("quadratic(2,3,1)=",quadratic(2,3,1))
if quadratic(2,3,1)!=(-0.5,-1):
  print("测试失败")
elif quadratic(1,3,-4)!=(1.0,-4.0):
  print("测试失败")
else:
  print("测试成功")

#默认参数的运用
def student(name,sex,age=6,city="beijing"): #age、city为默认参数 默认参数必须指向不变对象
  print("name:%s\n sex:%s\n age:%s\n city:%s" % (name,sex,age,city))

student("张三","男")
student("李四","男",7)
student("小红","女",city="云南")

#可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
#给定一组数字a,b,c...,计算a^2+b^2+c^2...
def calc(numbers):#非可变
  s=0
  for n in numbers:
    s=s+n**2
  return s

print(calc([1,2,3]))

def calc1(*numbers): #可变参数
  s=0
  for n in numbers:
    s=s+n**2
  return s

print(calc1(1,2,3))
print(calc1()) #传入0个参数
nums=[1,2,3]
print(calc1(*nums))

#关键字参数 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**other):
  print("name:",name,"age:",age,"other",other) #我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到

person("jack",30,city="beijing",job="engineer")
extra={"city":"beijing","job":"engineer"}
person("jack",30,**extra)

#命名关键字参数
def person1(name,age,*,city="beijing",job):#只接收city，job作为关键字参数,city有默认值可不传
  print(name,age,city,job)

person1("张三",40,city="anhui",job="teacher")
person1("张三",40,job="teacher")
#5种参数都可以组合使用,参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,d,**other):
  print("a=",a,"b=",b,"c=",c,"args=",args,"d=",d,"other=",other)
def f2(a,b,c=0,*,d,**other):
  print("a=",a,"b=",b,"c=",c,"d=",d,"other=",other)

f1(1,2,d="haha")
f1(1,2,3,"a","b",d="haha")
f1(1,2,3,d="haha",city="beijing",job="engineer")

f2(1,2,d="haha",gg="simida")

#可接收一个或多个数并计算乘积
def product(*nums):
  if len(nums)>0:
    s=1
    for n in nums:
      s=s*n
    return s
  else:
    raise TypeError()
#测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

#递归函数
#计算n!=1*2*3*...*(n-1)*n
def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

print(fact(1)) #1
print(fact(5)) #120