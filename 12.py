class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = []
        ans = ''
        for i in range(len(roman)):
            ans += (num // value[i]) * roman[i]
            num = num % value[i]
        return ans
