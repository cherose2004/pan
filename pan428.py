'''
请使用Python3编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格不用进行加
密处理。
'''
str1 = 'abcdefghijklmnopqrstuvwxyz'
m = 3
text = 'i love china!'
s = ''
for c in text:
    if c in str1:
        s += str1[(str1.index(c)-m)%26]
    else:
        s += c
print(s)