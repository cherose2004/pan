'''
一辆卡车违反交通规则，撞人逃逸。现场有三人目击事件，但都没有记住车号，只记下车号的一些特征。甲说：车号的前两位数字是相同的；乙说：车号的后两位数字是相同的，但与前两位不同；丙是数学家，他说：四位的车号刚好是一个整数的平方。请用Python语言根据以上线索求出车号。
'''

for i in range(0,10):
    for j in range(0,10):
        if i == j:
            continue
        else:
            num = i*1000+i*100+j*10+j
            # print(num)
            if pow(num,0.5) == int(pow(num,0.5)):
                print(num)
    