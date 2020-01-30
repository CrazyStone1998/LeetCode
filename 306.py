class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def _find(num):
            half_line = len(num) // 2 + 1
            third_line = (len(num) // 3) * 2 + 1
            for i in range(1, half_line):
                m_end = i
                for j in range(i + 1, third_line):
                    n_end = j
                    if num[0] == '0' and m_end > 1:
                        continue
                    if num[m_end] == '0' and (n_end - m_end) > 1:
                        continue
                    if _isValid(0, m_end, n_end, num):
                        return True
            return False

        def _isValid(m_start, mn_mid, n_end, num):

            s = int(num[m_start:mn_mid]) + int(num[mn_mid:n_end])
            s_s = str(s)
            s_end = len(s_s) + n_end
            if len(num) >= s_end and num[n_end:s_end] == s_s:
                if len(num) == s_end:
                    return True
                else:
                    return _isValid(mn_mid, n_end, s_end, num)
            else:
                return False

        return _find(num)
print(Solution().isAdditiveNumber('112358'))
