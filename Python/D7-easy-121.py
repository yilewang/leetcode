# from others codes. I failed to solve this problem.

def buysell(prices):
    start = prices[0]
    lmax = 0
    for price in prices[1:]:
        if price < start:
            start = price
        else:
            lmax = max(lmax, price-start)
    return lmax




prices = [1,2,3,6,6]

print(buysell(prices))