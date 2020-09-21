'''
print("试玩")   # 字符串
print(2333)     # 整数
print(2.3)      #小数
print(False)    #布尔值 Ture or false
print(())       #元祖
print([])       #数组
print({})       #字典
print("试玩"+"01")    #字符串拼接
print("试玩"*3)
print(1+2,3/2,4*5)    #数学运算
print(1+1==2,2>3)  
#变量 赋值
a="阿三"   # 把阿三这个值赋值给了叫a的变量
print(a)
'''
# a=float(input("请输入:"))      #input获取的都是字符串
# b=float(input("请输入:"))
# print("input获取的内容：",a+b)

#数据格式转换
# print(type(233))    #或者 x=type(233) print(c)
# print(type(2.33))
# print(type("233"))
# print(type(True))
# print(type(()))
# print(type({}))
# print(type([]))
# 任何数据都可以转换成字符串（除了空NoneType）,整数和小数可以互相转换
# 字符串转换为其他类型的数据，必须满足规定（比如长得像）
# a = int("2333")
# print(type(a))

# len 支持字符串、元祖、数组、字典
# a="dfghjkiuytfghjtfghjiuy"
# print(len(a))
a=input("输入内容1:")
b=input("输入内容2:")
print(len(a+b))