def coinchange(total:int, coins:list) -> int: # C(N, m)
    M = len(coins)
    coins.sort()
    if total == 0:
        return 1
    if total < 0 or M <= 0:
        return 0
    return coinchange(total, coins[:-1]) + coinchange(total-coins[-1], coins)

print(coinchange(10, [1,2,5]))