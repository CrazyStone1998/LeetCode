class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num = [0, 0, 0, 0, 0]

        for i in text:
            if i == 'b':
                num[0] += 1
            elif i == 'a':
                num[1] += 1
            elif i == 'l':
                num[2] += 1
            elif i == 'o':
                num[3] += 1
            elif i == 'n':
                num[4] += 1

        num[2] //= 2
        num[3] //= 2

        return min(num)
