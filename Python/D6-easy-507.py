import numpy as np

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        div_res = 0
        for i in range(1, int(num**(1/2)+1), 1):
            boo = (num % i == 0)
            if boo:
                div_res += i
                print(div_res)
                if i*i != num:
                    div_res += num/i
                    print(div_res)
        return div_res - num == num
        

a = Solution()
print(a.checkPerfectNumber(28))