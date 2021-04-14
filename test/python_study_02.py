#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#条件判断
s=input("请输入brith:")
birth=int(s)
if birth<2000:
  print("00前")
elif birth>2000 and birth<2010:
  print("00后")
elif birth==2000:
  print("牛逼！！！")
else:
  print("10后")

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height=input("请输入身高（单位m）：")
weight=input("请输入体重（单位kg）：")
w=float(weight)
h=float(height)
bmi=w/h**2
print(bmi)
if bmi<18.5:
  print("过轻")
elif bmi>=18.5 and bmi<25:
  print("正常")
elif bmi>=25 and bmi<28:
  print("过重")
elif bmi>=28 and bmi<32:
  print("肥胖")
else:
  print("严重肥胖")


#循环语句

#for...in循环，依次把list或tuple中的每个元素迭代出来
#计算1~10的整数之和
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
  sum=sum+x
print(sum)
#计算1~100的整数之和
#range()函数可以生成一个整数序列，再通过list()函数可以转换为list
sum=0
for x in range(101):
  sum=sum+x
print(sum)

#while循环
#计算100以内奇数之和
sum1=0
n=99
while n>0:
  sum1=sum1+n
  n=n-2
print(sum1)
#break可以提前结束循环 continue可以跳过此次循环
a=1
while a<=10:
  if a>5:
    break  #直接结束循环
  print(a)
  a=a+1
print("END")

b=0
while b<10:
  b=b+1
  if b%2==0:
    continue  #可以跳过此次循环
  print(b)




