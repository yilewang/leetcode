

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = False
        text = ''.join(re.split("[^a-zA-Z0-9]*", s))
        if text == "":
            res = True
        if text.lower() == text[::-1].lower():
            res = True
        return res     

s = " "

print(isPalindrome(s))
