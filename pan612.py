'''
一元三次方程式有各种解法，请用Python语言编写一函数，实现用牛顿迭代法求方程ax^3+bx^2+cx+d=0在x=1附近的一个实根。主函数完成各系数值的输入及所求得的根值的输出。
'''


def Newton_Method(a,b,c,d,x):
    x0 = x
    while True:
        f = a*x0**3 + b*x0**2 + c*x0 + d
        f_d = 3*a*x0**2 + b*x0 + c
        x = x0
        x0 = x0 - f/f_d
        print(x," ",x0)
        if abs(x0-x) <= 1e-5:
            return x0

print(Newton_Method(9,0,1,4,5))