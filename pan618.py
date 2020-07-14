'''
一辆以固定速度行驶的汽车，司机在上午10点看到里程表上的读数是一个对称数(即这个数从左向右读和从右向左读是完全一样的)，为95859。两小时后里程表上出现了一个新的对称数（95859的下一个），该数字仍为五位数。问该车的速度是多少？新的对称数是多少？
'''

number_first = 95859
while True:
    number_first += 1
    if str(number_first) == str(number_first)[::-1]:
        break
print("车速为{}公里/小时，新的对称数为{}。".format((number_first-95859)/2,number_first))