'''
小松鼠采集松果，晴天每天可以采集20个，雨天每天可以采集12个。一连几天它一共采了112个松果，平均
每天采14个，请问这些天有几天下雨了？请使用Python3编程解题。
'''

i,j = 0,0
n = 112//12
while i<=n:
    for j in range(n):
        if i*20+j*12==112 and 112/(i+j) == 14:
            print(j)
    i+=1
