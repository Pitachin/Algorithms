"""
Problem: http://www.algorithmist.com/index.php/Coin_Change
"""
def coinchange(total, coins):
    M = len(coins)
    table = [[0]*M for i in range(total+1)]
    for i in range(M):
        table[0][i] = 1

    for i in range(1, total+1):
        for j in range(M):
            # count of solutions excluding coin
            x = table[i][j-1] if j > 0 else 0

            # count of solutions including coin
            y = table[i-coins[j]][j] if i - coins[j] >= 0 else 0
            table[i][j] = x + y

    return table[total][M-1]

if __name__ == "__main__":
    print(coinchange(10, [2, 3, 5, 6])) # 5
    print(coinchange(5, [2, 3, 5]))     # 2
    print(coinchange(4, [1, 2, 3]))    # 4


"""

N = 4, coins = [1,2,3]
[
    [C(1,1), C(1,2), C(1,3)],
    [C(2,1), C(2,2), C(2,3)],
    [C(3,1), C(3,2), C(3,3)],
    [C(4,1), C(4,2), C(4,3)],
    [C(5,1), C(5,2), C(5,3)],
]

C(N, m) = C(N, m-1) + C(N - coins[m-1], m)
"""