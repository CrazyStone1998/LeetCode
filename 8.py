class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1                # 整数符号　+1 or -1
        ans = 0                 # 累计结果
        FirstCharCheck = True   # bool 用于检测第一个非空格字符，默认为Ｔrue,当检测到第一个字符后设为 False
        for i in range(len(str)):
            if FirstCharCheck:
                if str[i] == ' ':                         # 遇到空格跳过，直到遇到第一个非空格字符
                    continue
                elif str[i] == '-' or str[i] == '+':      # 如果第一个字符为+/-号, 更新sign,
                    sign = 44-ord(str[i])
                    if i+1 < len(str) and not str[i+1].isdigit():   # 判定+/-后字符是否为数字
                        return 0
                elif str[i].isdigit():                     # 如果第一个字符为数字，更新ans
                    ans = ans*10+ord(str[i]) - ord('0')
                else:                                      # 第一个字符为其他符号，return
                    return 0
                FirstCharCheck = False                     # 判定第一个字符后，更新FirstCharCheck,避免重复检测

            elif str[i].isdigit():                         # 后续遇到数字字符，累加到ans
                ans = ans * 10 + ord(str[i]) - ord('0')
            else:                                          # 后续遇到非数字字符，直接break,计算结果
                break
        ans *= sign                                        # 计算结果
        if ans < -2 ** 31:
            return -2 ** 31
        if ans >= 2 ** 31:
            return 2 ** 31 - 1
        return ans
