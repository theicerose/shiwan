# 文件读写
import time
now=time.strftime('%y-%m-%d-%H:%M:%S')
print(now)
text=input('请输入内容：')
# with open('日记.txt','w',encoding='utf8') as t:  #utf8是格式，让写入的内容中文
#w是写入，每次都会清空以前的内容
with open('日记.txt','a',encoding='utf8') as t:
    #a是追加
    # t.write(text)

    # \t 中间空白隔开
    # \n 直接换行
    t.write('\n'+now+'\n'+text+'\n'+'---------------')