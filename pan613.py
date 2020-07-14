'''
假设某银行一年整存零取得月息为0.63%，现某人手中有一笔钱，他打算在今后的五年中，每年年底取出1000元，到第5年刚好取完，请用Python语言算出此人存钱时应该存入多少？
'''

monthly_Interest = 0.0063
money = 5000

while money>=0:
    guess = money
    for j in range(1,6):
        guess = guess*(1+monthly_Interest*12)-1000
        print(guess)
    if abs(guess) <= 1:
        print(money)
        break
    money -= 1



