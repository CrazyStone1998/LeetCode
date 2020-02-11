class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_reverse = 0
        temp = x
        while temp > 0:
            x_reverse = x_reverse * 10 + temp % 10
            temp //= 10
        return x_reverse == x

print(Solution().isPalindrome(121))