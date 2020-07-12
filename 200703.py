'''
请用Python语言编程，从小到大输出所有4位数的可逆素数（为了美观整洁，每行输出20个）。可逆素数的定义是：一个素数将其各位数字的顺序倒过来构成的反序数也是素数。
'''
import math

def isPrimes(num):
    for i in range(2,math.ceil(math.sqrt(num))):
        if num%i == 0:
            return False
    return True

def main():
    for i in range(1000,10000):
        if isPrimes(i):
            if isPrimes(int(str(i)[::-1])):
                print(i,' ', end='')

if __name__ == "__main__":
    main()


