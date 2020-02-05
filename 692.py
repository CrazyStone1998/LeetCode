from collections import Counter
class Solution:

    def topKFrequent(self, words, k: int):
        return [i[0] for i in sorted(Counter(words).items(), key=lambda x: (x[1], x[0]))[:k]]
