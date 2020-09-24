'''类 class
class声明类的名字，然后类的名字首字母必须大写
面向对象编程
类里面必须要传一个参数，叫self
'''
# class Shiwan():                #这个写法是固定的  
#     '''
#     小游戏
#     '''
#     def __init__(self,name,typr,mode,age):            #也是固定的,且每个方法第一个参数必须是self
#         #self指类自身，这里self就是指Shiwan
#         self.name='种田'                          
#         self.type='rpg'
#         self.mode='single'
#         self.age='17+'
#     def mubiao(self,h):
#         '''
#         游戏基本功能
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         if h==1:
#             print('牧场种田')
#         elif h==2:
#             print('交友')
#         else:
#             print('钓鱼')
#     def daguai(self):
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         '''游戏打怪
#         '''
#         print('打史莱姆')
#     def tiaozhan(self):
#         '''游戏挑战模式
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         print('打小BOSS')

# 类的实例化
# a=Shiwan()       #这一步就是把类实例化
# a.mubiao(2)
# a.daguai()
# a.tiaozhan()
# print(a.age)

# class Shiwan():                #这个写法是固定的  
#     '''
#     小游戏
#     '''
#     def __init__(self,name,leixing,mode,age):            #用参数控制属性
#         self.name=name
#         self.leixing=leixing     
#         self.mode=mode
#         self.age=age
#     def mubiao(self,h):
#         '''
#         游戏基本功能
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         if h==1:
#             print('牧场种田')
#         elif h==2:
#             print('交友')
#         else:
#             print('钓鱼')
#     def daguai(self):
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         '''游戏打怪
#         '''
#         print('打史莱姆')
#     def tiaozhan(self):
#         '''游戏挑战模式
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         print('打小BOSS')
# a=Shiwan('3A大作','回合制','多人组队','18+')    #自定义参数
# a.mubiao(2)
# a.daguai()
# a.tiaozhan()
# print(a.age)

# class Zhujue():
#     def __init__(self,xingbie,wuqi,zuoqi,huoban):
#         self.xingbie=xingbie
#         self.wuqi=wuqi
#         self.zuoqi=zuoqi
#         self.huoban=huoban
#     def renwu(self):
#         print('你的主角完成了一个任务')
#     def caiji(self):
#         print('你的主角采集到了一朵花')
#     def diaoyu(self):
#         print('等了十分钟，你的主角钓到了一条小鱼')

# xiaohei=Zhujue('男','大剑','狗子','老爷')
# xiaohei.renwu()
'''
#类的特点：继承、重写
'''
# class Shiwan():                #这个写法是固定的  
#     '''
#     小游戏
#     '''
#     def __init__(self,name,leixing,mode,age):            #用参数控制属性
#         self.name=name
#         self.leixing=leixing     
#         self.mode=mode
#         self.age=age
#     def mubiao(self,h):
#         '''
#         游戏基本功能
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         if h==1:
#             print('牧场种田')
#         elif h==2:
#             print('交友')
#         else:
#             print('钓鱼')
#     def daguai(self):
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         '''游戏打怪
#         '''
#         print('打史莱姆')
#     def tiaozhan(self):
#         '''游戏挑战模式
#         '''
#         print('你的名叫'+self.name+'，并且游戏类型为'+self.leixing+'，游戏模式为'+self.mode+'，游戏限制为'+self.age+'的游戏里面，主角开始去：')
#         print('打小BOSS')

#继承
# class Neice(Shiwan):             #类(Neice)继承了(Shiwan)的规则
# '''Shiwan 为父类
#    Neice  为子类
#    这里，子类继承了父类所有的东西
# '''
#     pass
# aerfa=Neice('十万大作','手游','抽卡','0+')
# aerfa.daguai()

#重写
# class Neice(Shiwan):
#     def tiaozhan(self):
#         print('开始打幕后BOSS')
# '''把父类里面的tiaozhan规则重写为新的规则'''
# '''object为所有类的祖宗
# class Shiwan()括号内虽然没东西，其实是继承了object的，即class Shiwan()就等于
# class Shiwan(object)
# '''

# aerfa=Neice('十万大作','手游','抽卡','0+')
# aerfa.tiaozhan()
# aerfa.daguai()