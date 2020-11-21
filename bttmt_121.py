def max_profit(prices):
    rx = 0
    leng = len(prices)
    if leng == 0:
        return rx

    vmap = dict()  # 중복 요소 있을 시, 인덱스를 덮어써버려 해결이 어려움.
    for i, n in enumerate(prices):
       vmap[n] = i
    # for i in range(leng-1, -1, -1):
    #     n = prices[i]
    #     vmap[n] = i
    prices = sorted(prices)
    print(prices)

    for max_i in range(leng-1, 0, -1):
        mx = prices[max_i]
        for min_i in range(0, leng-1):
            if min_i == max_i:
                break
            mi = prices[min_i]
            if vmap[mi] < vmap[mx]:
                return mx - mi
            else:
                pass
    return rx


def max_profit_sol(prices):
    mi = float('inf')
    mx = 0
    print(prices)
    print(f'i=none, mi={mi} mx={mx} prices[i]=none')
    for i, n in enumerate(prices):
        if prices[i] < mi:
            mi = prices[i]
        elif (prices[i] - mi) > mx:
            mx = prices[i]-mi;
        print(f'i={i}, mi={mi} mx={mx} prices[i]={prices[i]}')
    return mx


def max_profit_brute(prices):
    leng = len(prices)
    rx = 0
    for i in range(leng-1,-1,-1):
        for z in range(0, i+1):
            c_diff = prices[i]-prices[z]
            if c_diff > rx:
                rx = c_diff
    return rx