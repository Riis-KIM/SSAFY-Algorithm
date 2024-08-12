# 그리디 알고리즘


T = int(input())
for test_case in range(1, T+1):
    # 50000, 10000, 5000, 1000, 500, 100, 50, 10
    won = [0] * 8

    money = int(input())

    # 5만원
    won[0] += money // 50000
    money %= 50000

    # 1만원
    won[1] += money // 10000
    money %= 10000

    # 5천원
    won[2] += money // 5000
    money %= 5000

    # 1천원
    won[3] += money // 1000
    money %= 1000

    # 5백원
    won[4] += money // 500
    money %= 500

    # 1백원
    won[5] += money // 100
    money %= 100

    # 50원
    won[6] += money // 50
    money %= 50

    # 10원
    won[7] += money // 10
    money %= 10

    print(f"#{test_case}")
    print(*won)

