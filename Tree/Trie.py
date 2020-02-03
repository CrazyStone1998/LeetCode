class TrieNode:

    def __init__(self):
        self.path = 0
        self.end = 0
        self.next = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

        self.root.path += 1

    def _pos(self, ch):
        return ord(ch) - ord('a')

    def insert(self, s):
        temp = self.root
        for i in s:
            if not temp.next[self._pos(i)]:
                temp.next[self._pos(i)] = TrieNode()
            temp = temp.next[self._pos(i)]
            temp.path += 1
        temp.end += 1

    def search(self, s):
        if s:
            temp = self.root
            for i in s:
                if temp.next[self._pos(i)]:
                    temp = temp.next[self._pos(i)]
                else:
                    return False

            if temp.end > 0:
                return True

        return False

    def delete(self, s):
        if self.search(s):
            temp = self.root
            for i in s:
                temp.next[self._pos(i)].path -= 1
                if temp.next[self._pos(i)].path == 0:
                    temp.next[self._pos(i)] = None
                    return
                temp = temp.next[self._pos(i)]
            temp.end -= 1
