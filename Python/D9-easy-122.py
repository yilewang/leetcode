
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ini_p = prices[0]
        pro = 0
        for i in prices:
            while i >ini_p:
                pro += i -ini_p
                ini_p = i
            else:
                ini_p = i
        return pro
        


prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))
