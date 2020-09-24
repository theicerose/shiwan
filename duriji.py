
with open('E:\pytest\github-1\shiwan\日记.txt','r',encoding='utf8') as e:
    text=e.readlines()
    for i in text:               #这个读法读出来是数组，所以可以遍历
        print(i)