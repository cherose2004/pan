'''
现在我们需要将5元人民币纸币兑换成1元、5角和1角的硬币，请用Python语言计算出共有多少种不同的兑换方法。
'''
count = 0
for i in range(6):
    for j in range(11):
        for k in range(51):
            if i*1 + j*0.5 + k*0.1 == 5:
                print("一元{}张，5角{}张，1角{}个".format(i,j,k))
                count += 1
print("共有{}种兑换方法".format(count))

