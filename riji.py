import time
now=time.strftime('%y-%m-%d-%H:%M:%S')
text=input('请输入内容：')
with open('E:\日记.txt','a',encoding='utf8') as t:
        t.write('\n'+now+'\n'+text+'\n'+'---------------')