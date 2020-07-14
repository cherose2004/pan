'''
小明把一缸金鱼分5次出售：第1次卖出全部的一半加1/2条；第2次卖出余下的三分之一加1/3条；第3次卖出余下的四分之一加1/4条；第4次卖出余下的五分之一加1/5条；最后卖出余下的11条。请用Python语言编程求出原来鱼缸中共有多少条鱼。
'''

sum_num,total =  11,11
while True:
    total = sum_num
    for i in range(2,6):
        total = total - (total*(1/i) + (1/i)) 
    if total == 11:
        print(sum_num)
        break
    sum_num = sum_num + 1
