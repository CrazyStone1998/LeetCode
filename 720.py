class Solution:
    def longestWord(self, words) -> str:
        dic = {}
        result = []
        for i in range(1, 31):
            dic[i] = []
        for i in words:
            dic[len(i)].append(i)
        for i in range(2, 31):
            pre_del = set()
            pre_mid = set()
            if dic[i - 1] == []:
                dic[i] = []
                continue
            for j in dic[i]:
                if j[:-1] in dic[i - 1]:
                    pre_del.add(j[:-1])
                else:
                    pre_mid.add(j)
            for k in pre_mid:
                dic[i].remove(k)
            for k in pre_del:
                dic[i - 1].remove(k)
        for k, value in dic.items():
            result.extend(value)
        return sorted(result, key=lambda x: (-len(x),x))[0]
