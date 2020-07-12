'''
请用Python语言编程，计算下列多项式的值。比如说，从键盘上输入50后，输出为1.718282。
'''
import math

sum = 0
for i in range(1,50):
    sum = sum + 1/(math.factorial(i))

print(sum)
