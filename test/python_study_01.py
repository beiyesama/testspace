#当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

#!/usr/bin/env python3
# -*- coding: utf-8 -*-




print ("hello world!","aoligei","yigeiwoligiaogiao")
print(100)
print(100+200)
print("100+200=",100+200)

name=input("请输入姓名：")
print("姓名是",name)     #姓名是 张三
print("姓名是%s" % name) #姓名是张三

#如果字符串内部既包含'又包含"，用转义字符\来标识
print("I\'m \"OK\"!\nand you?")
print("\\\n\\")
print("\\\t\\")
print(r'\\\t\\') #r''表示''内部的字符串默认不转义
print('''line1
line2
line3''')
print(r'''line1\n
line2
line3''')

#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a=123 #a是整数
print(a)
a="hello" #a变为字符串
print(a)


print("包含中文的str")
print(ord("A"))   #65
print(chr(66))   #B

#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
#Unicode表示的str通过encode()方法可以编码为指定的bytes
print("ABC".encode("ascii")) #b'ABC'
print("中文".encode("utf-8")) #b'\xe4\xb8\xad\xe6\x96\x87'
#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'ABC'.decode("ascii")) #ABC
print(b'\xe4\xb8\xad\xe6\x96\x87\xad'.decode("utf-8",errors="ignore")) #中文

#要计算str包含多少个字符，可以用len()函数
print(len("ABC"))  #3
print(len("中文")) #2
#如果换成bytes，len()函数就计算字节数
print(len(b'ABC')) #3
print(len("中文".encode("utf-8"))) #6
#可见 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

#格式化 %s表示用字符串替换，%d表示用整数替换,%f表示浮点数替换，
print("hello,%s" % "world")
print("hello,%s,you have $%d" % ("Michael",10000))
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print("%2d-%03d" % (3,1)) # 3-001
print("%.2f" % 3.1415926) #3.14
print("growth:%d%%" % 7) #%%表示%

#格式化 f-string 使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r=2.5
s=3.14*r**2
print(f"半径为{r}的圆的面积是{s:.2f}")

#列表：list是一种有序的集合，可以随时添加和删除其中的元素
classmates=["andi","bob","jack"]
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.append("tom") #往list中追加元素到末尾
print(classmates[3])
classmates.insert(1,"jerry") #在指定位置插入元素
print(classmates[1])
classmates.pop(3) #删除指定位置的元素
classmates[0]="july" #替换直接赋值
print(classmates)
print(classmates[0:3])#不包括classmates[3]

L=["jack",123,True,["java","python"]]
print(L[3][1])

#元组：tuple tuple一旦初始化就不能修改
friend=("jack",1,True)
#只有1个元素的tuple定义时必须加一个逗号,来消除歧义
s=() #定义一个空tuple
t=(1,)
print(t)

#字典：dict
d={"michael":95,"bob":75,"lucy":80}
print(d["michael"])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d["jack"]=60
print(d)
#多次对一个key放入value，后面的值会把前面的值冲掉
d["jack"]=70
print(d["jack"])
#判断key是否存在
print("tomas" in d) #False
print(d.get("bob","不存在") )#75
print(d.get("tomas","不存在")) #不存在
#删除一个key
d.pop("jack")
print("jack" in d) #False

