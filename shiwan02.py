#判断 代码块
# a=1                #一个等号是赋值
# b=2
# if a==1:            #2个等号是判断
#     print('good')
# #判断符号 ==等于,!=不等于,>大于,<小于,in在里面,is是,not in不在里面,not is不是
# if a>b:
#     print('a比b大')#必须4空格  叫缩进(实际好像没效果)
# else:
#     print('b大于a')

# age=int(input('输入你的年龄：'))
# if age>60:
#     print('退休')           #从上至下，满足后就立刻运行，不管后面的
# elif age>30:
#     print('努力工作')
# elif age>20:
#     print('规划下吧')
# else:
#     print('好好学习')

# a=input('请输入：')       #exit   退出
# if a=='':
#     print('不能为空')
#     exit()
# if a in '0123456789':
#     a=int(a)
# else:
#     print('请输入数字')
#     exit()
# if a>5:
#     print('符合')
# else:
#     print('不符合')

# a=10
# if type(a) is int:
#     print('a是数字')
# elif type(a) is str:
#     print('a是字符串')
# else:
#     print('其他')

#循环
#while循环
# a=1
# while a<10:
#     print('good',a)
#     a=a*2
'''练习：现在有10个学生的成绩要录入系统中
这10个人分别是a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
并且名字和成绩需要对应上
而且大于60的和小于60的需要分开存放'''
# a=0
# b={}
# c={}
# while a<10:
#     d=input('输入姓名：')
#     e=int(input('输入成绩：'))
#     a=a+1
#     if e<60:
#         b[d]=e
#     else:
#         c[d]=e

# print('不及格的为',b)
# print('及格的为',c)

# bujige={}
# jige={}
# xuesheng=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
# a=0
# while a<len(xuesheng):                  #a为数组内全部下标值
#     chengji=int(input('请输入'+xuesheng[a]+'的成绩：'))
#     if chengji>=60:
#         jige[xuesheng[a]]=chengji
#     else:
#         bujige[xuesheng[a]]=chengji
#     a=a+1                    
# print('不及格的：',bujige)
# print('及格的：',jige)

#for循环 通过遍历来实现 
#rang()  数列生成器
# a='爱神的箭哈会计师发卡机房'
# for i in a:
#     print(i)

# b=list(range(3,100,2))  #自动生成一个数列，步进/步长默认1
# print(b)
# for i in range(20):
#     print(i)

#第50行新做法
# bujige={}
# jige={}
# xuesheng=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
# for i in xuesheng:
#     chengji=int(input('请输入'+i+'的成绩：'))
#     if chengji<60:
#         bujige[i]=chengji
#     else:
#         jige[i]=chengji
# print('不及格的名单',bujige)
# print('及格的名单',jige)

'''练习，打印九九乘法表'''
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(a,'X',b,'=',a*b,end='  ')    #end控制不换行
#     print()

# for i in range(20):
#     print(i,end='@@')
# print('----------')
'''练习1
通过print打印模拟红绿灯功能，红灯30次，绿灯35次，黄灯3次。
练习2
使用代码实现一个注册功能，用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号
必须小写字母开头，储存到字典中{username:password}
'''
# a={'红灯':30,'绿灯':35,'黄灯':3}
# while True:                #加上这句就会死循环
# for i in a:
#     for j in range(a[i]):
#         print(i,'剩余',a[i]-j,'秒')
# a=input('请输入账号：')
# b=input('请输入密码：')
# if len(a)>=5 and len(a)<=8:
#     if a[0] in 'qwertyuiopasdfghjklzxcvbnm':
#         if len(b)>=6 and len(b)<=12:
#             print('账号创建成功',{a:b})
#         else:
#             print("密码长度必须为6-12位")
#     else:
#         print('账号必须以小写字母开头')
# else:
#     print('账号的长度必须为5-8位')

# for i in range(10):
#     if i==4:
#         continue               #continue 跳过当前循环，从头继续
#     print(i)

# for i in range(10):
#     if i==4:
#         break                 #break  直接跳出循环
#     print(i)

# for a in range(1,10):
#     for b in range(1,a+1):
#         if a==5:
#             break                               #只跳出一层循环
#         print(a,'X',b,'=',a*b,end='  ')    
#     print()

# 函数/方法
# def checkname(un):       #def方法声明，checkname方法的名字，un方法的参数(参数可以没有)
#     '''    
#     账号长度是5-8位，并且账号必须小写字母开                
#     '''                                                  #自定义函数写说明
#     if len(un)>=5 and len(un)<=8:                        #下面都是方法的逻辑代码
#         if un[0] in 'qwertyuiopasdfghjklzxcvbnm':
#             print('ok')
#         else:
#             print('账号必须以小写字母开头')
#     else:
#         print('账号的长度必须为5-8位')
# checkname('ataaa')

#返回值，返回后我们可以对这个值做其他的操作
#而，print不可以
# a=[1,2,3,4,5,6,7,8]
# x=a.index(3)
# print(a[x])

# def checkname(un):       #def方法声明，checkname方法的名字，un方法的参数(参数可以没有)
#     '''    
#     账号长度是5-8位，并且账号必须小写字母开                
#     '''                                                  #自定义函数写说明
#     if len(un)>=5 and len(un)<=8:                        #下面都是方法的逻辑代码
#         if un[0] in 'qwertyuiopasdfghjklzxcvbnm':
#             return True                      #有return的返回值，才能print出来
#         else:
#             return '账号必须以小写字母开头'
#     else:
#         return '账号的长度必须为5-8位'
# un=input('请输入账号：')
# pw=input('请输入密码：')
# if checkname(un)==True:
#     if len(pw)>=6 and len(pw)<=12:
#         print('账号创建成功',{un:pw})
#     else:
#         print("密码长度必须为6-12位") 
# else:
#     print(checkname(un))

# 代码报错就是异常
# try:
#     print(1+1)
#     print('1'+1)
#     print(1+4)
# except Exception as e:
#     print('上面代码错了',e)

#异常类    包->类->方法->变量（既包含，又并列）

# a=input('输入你的姓名：')
# b=input('输入你的年龄：')
# try:                                    #用来控制用户的输入，比如输入年龄“十八”
#     if int(b)>18:
#       print(a,'成年了')
#     else:
#         print(a,'未成年')
# except:
#     print('请输入正确的年龄')

import time                    #time包  时间
import random                  #random  生成随机数
import pymysql
# for i in range(10):
#     time.sleep(1)
#     print(i)

# a=random.randint(10,1000)
# print(a)

# pip管理第三方包
#pip install 包名  加载第三方的包
#pip uninstall 包名  卸载
#pip list      查看加载了多少第三方包
#
#常用的第三方包：
#pymysql   操作mysql的包
#selenium   做web自动化的包
#appium     做app自动化的包
#requests   做接口自动化的包
#xlrd       操作exl的包
#xlwt       写入EXL的包

'''练习：定义一个方法，判断用户输入的账号密码是否符合规范'''
def checknp():
    a=input('请输入账号：')
    b=input('请输入密码：')
    if len(a)>=5 and len(a)<=8:
        if a[0] in 'qwertyuiopasdfghjklzxcvbnm':
            if len(b)>=6 and len(b)<=12:
                print('账号创建成功',{a,b})
            else:
                print('密码长度必须为6-12位')
        else:
            print('账号的第一位必须为小写字母')
    else:
        print('账号长度必须5-8位')

checknp()
