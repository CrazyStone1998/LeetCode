class Solution:
    def splitIntoFibonacci(self, S: str):
        if len(S) < 3:
            return []
        else:
            return self._split(S)

    def _match(self, m, n, rest, result):

        if m[0] == '0' and len(m) != 1:
            return False
        elif n[0] == '0' and len(n) != 1:
            return False
        elif rest[0] == '0' and (m != '0' or n != '0'):
            return False
        else:
            s = str(int(m) + int(n))
            if int(s) >= (2**31 -1):
                return False

            lr = len(rest)
            ls = len(s)
            if lr >= ls and rest[:len(s)] == s:
                result.append(int(n))
                if lr == ls:
                    result.append(int(s))
                    return True
                else:
                    return self._match(n, s, rest[ls:], result)
            else:
                return False

    def _split(self, S):
        l = len(S)
        mid = (l // 3) * 2 + 1
        half = S[:mid]
        for i in range(1, mid):
            m = half[:i]
            for j in range(i+1, mid+1):
                n = half[i:j]
                result = [int(m), ]
                key = self._match(m, n, S[j:], result)
                if key:
                    return result
        return []
