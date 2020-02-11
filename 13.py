class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        ans = 0
        value = 1
        for i in s[::-1]:
            if roman[i]>=value:
                ans += roman[i]
                value = roman[i]
            else:
                ans -= roman[i]
        return ans