class Node:
    def __init__(self, flag=None, value=0, left_child=None, right_child=None):
        self.flag = flag
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class Huffman:

    def __init__(self, text):
        self.arr = self.pretreatment(text)
        self.code = {}

    def pretreatment(self, text):
        d = {}
        for i in text:
            d[i] = d.get(i, 0) + 1
        print(d)
        return d

    def huffman(self):
        minHeap = MinHeap(arr=self.arr)
        for i in range(len(self.arr) - 1):
            x = minHeap.pop()
            y = minHeap.pop()
            z = Node(value=x.value + y.value, left_child=x, right_child=y)
            minHeap.insert(z)
        self.huffman_dfs(minHeap.heap[0], '')
        return self.code
    def huffman_dfs(self, root: Node, s):
        if root.flag:
            self.code[root.flag] = s
        else:
            self.huffman_dfs(root.left_child, s + '0')
            self.huffman_dfs(root.right_child, s + '1')

class MinHeap:

    def __init__(self, arr):
        self.heap = [None for _ in range(len(arr))]
        self.size = 0

        for i, j in arr.items():
            self.insert(Node(flag=i, value=j))

    def insert(self, data):
        self.heap[self.size] = data
        self._up(self.size)
        self.size += 1

    def pop(self):
        result = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self._down(0)
        return result

    def _down(self, pos):

        while True:
            child = 2 * pos + 1
            if child > self.size - 1:
                break
            if child + 1 < self.size and self.heap[child + 1].value < self.heap[child].value:
                child = child + 1
            if self.heap[pos].value < self.heap[child].value:
                break
            else:
                self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
                pos = child

    def _up(self, pos):

        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[parent].value > self.heap[pos].value:
                self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
            else:
                break
            pos = parent
