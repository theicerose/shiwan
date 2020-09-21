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
# a=input("输入内容1:")
# b=input("输入内容2:")
# print(len(a+b))

# print("试玩")   # 字符串
# print(2333)     # 整数
# print(2.3)      #小数
# print(False)    #布尔值 Ture or false Ture=1,False=0
# print(())       #元祖
# print([])       #数组
# print({})       #字典
# print("试玩"+"01")    #字符串拼接
# print("试玩"*3)
# print(1+2,3/2,4*5)    #数学运算
# print(1+1==2,2>3) 

#元祖  下标，从0开始编号
# a=(2,34,67,8,2348,3,5,7,34,6,2,577,'来玩哟','骚年',True,False)
# a[4]
# b=(a,'骚年','骚年',57)
# print(a),print(a[4])
#print(a.index(2))
# index 搜索从左往右第一个数据的下标
# print(a.count(2)) count 计算元祖里有几个2
#print(b[0][4])   #层层递进，一层层下标定位

#切片
#print(a[0:6])   #左闭右开，从0到第5个
#print(a[7:])

#元祖写好后不可修改，数组是可以修改的
#数组
# a=[2,34,67,8,2348,3,5,7,34,6,2,577,'来玩哟','骚年',True,False]
#a.append('小意思')  append 往数组中追加数据（在最尾部）
#a.insert(0,'开头')   insert 往数组中指定位置插入数据,0是下标位置
# a.pop(-4)            #   pop 剪切（-4是下标位置）剪切后原数组就失去该数据
# b=a.pop(-4)          #pop剪切出去的可以给其他变量赋值
# a.clear()       clear 清空
# xx=['完蛋',123,1]         
# a.extend(xx)             extend可以加入数组，用a+xx也能实现
# print(a)
#所有的方法都是小括号结尾，元祖、数组、字典的取值都是中括号

#字典的特点
#1、字典中的值无顺序
#2、字典的结构必须是 键值对的结构（key:value)
# a={'name':'猎天使','gametime':8,0:'哟'}
# print(a['name'])
# a['sc']='190'               增加
# a['name']='堕落天使'          修改
# b=a.get('name')               取值
# c=a.pop(0)                    剪切
# a.update(name='恶魔')         新增、修改
# print(c,b,a)

#数组和字典的删除
# del a['name']
# del a[2]

#练习，获取用户输入的个人信息，并且输入到字典中，包括：name,age,sex

# a={}
# b=input('请输入姓名:')
# c=input('请输入年龄:')
# d=input('请输入性别:')
# a.update(name=b,age=c,sex=d)
# print(a)