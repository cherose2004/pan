'''
如果整数A的全部因子（包括1，不包括A本身）之和等于B，且整数B的全部因子（包括1，不包括B本身）之和等于A，则将整数A和B称为亲密数。请用Python语言编程，求3000以内的全部亲密数。
'''

n=int(input('Please input a integer: '))
num=n    #使用num变量保留输入的原始数值
m=[]
while n!=1:    #n==1时，已分解到最后一个质因数
    for i in range(2,int(n+1)):
        if n % i == 0:
            m.append(str(i))    #将i转化为字符串再追加到列表中，便于使用join函数进行输出
            n = n/i
    if n==1:
        break    #n==1时，循环停止
print(num,'=','×'.join(m))