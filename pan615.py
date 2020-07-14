'''
10个小孩围成一圈分糖果。老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，第5个小孩16块，第6个小孩4块，第7个小孩10块，第8个小孩6块，第9个小孩14块，第10个小孩20块。然后所有的小孩同时将手中的糖分一半给右边的小孩。糖块为奇数的人可向老师再要一块。请用Python语言编程序计算，经过几次这样的操作后，大家手中的糖块数能一样多？每人各有多少糖块？
'''

import numpy as np
children = [10,2,8,22,16,4,10,6,14,20]
candy_num = [10,2,8,22,16,4,10,6,14,20]
count = 0
while True:
    for i in range(0,10):
        candy_num[i] = children[i]/2
    for i in range(1,10):
        children[i] = candy_num[i-1] + children[i]/2
    children[0] = candy_num[9] + children[0]/2
    for i in range(0,10):
        if children[i]%2 != 0:
            children[i] = children[i] + 1
    if np.var(children) == 0:
        print(children)
        print(count)
        break
    count += 1