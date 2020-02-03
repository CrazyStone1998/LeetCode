from queue import Queue
from queue import LifoQueue as stack
import math


class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 1


class BinaryTree:

    def __init__(self):
        self.root = None
        self.size = 0

    @classmethod
    def init_by_arr(cls, arr):
        pass

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_height(self, node: Node):
        if not node:
            return 0
        else:
            return node.height

    def _balance_factor(self, node: Node):
        if not node:
            return 0
        else:
            return self.get_height(node.left_child) - self.get_height(node.right_child)

    def _balance(self, node: Node):
        if not node:
            return True
        elif abs(self._balance_factor(node)) > 1:
            return False
        else:
            return self._balance(node.left_child) and self._balance(node.right_child)

    def is_balanced(self):
        return self._balance(self.root)

    def _right_rotate(self, node):
        temp = node.left_child
        node.left_child = temp.right_child
        temp.right_child = node

        temp.height = max(self.get_height(temp.left_child), self.get_height(temp.right_child))
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child))
        return temp

    def _left_rotate(self, node):
        temp = node.right_child
        node.right_child = temp.left_child
        temp.left_child = node

        temp.height = max(self.get_height(temp.left_child), self.get_height(temp.right_child))
        node.height = max(self.get_height(node.left_child), self.get_height(node.right_child))
        return temp

    def _visit(self, node):
        print(node.data)

    def pre_order(self, root):

        if root:
            self._visit(root)
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)

    def preOrder(self, root):

        if not root:
            return
        s = stack()
        temp = root
        while temp or not s.empty():
            while temp:
                self._visit(temp)
                s.put(temp)
                temp = temp.left_child
            if not s.empty():
                temp = s.get()
                temp = temp.right_child

    def in_order(self, root):

        if root:
            self.in_order(root.left_child)
            self._visit(root)
            self.in_order(root.right_child)

    def inOrder(self, root):

        if not root:
            return
        s = stack()
        temp = root
        while temp or not s.empty():
            while temp:
                s.put(temp)
                temp = temp.left_child
            if not s.empty():
                temp = s.get()
                self._visit(temp)
                temp = temp.right_child

    def post_order(self, root):
        if root:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            self._visit(root)

    def postOrder(self, root):
        if not root:
            return
        s1 = stack()
        s2 = stack()
        s1.put(root)

        while not s1.empty():
            temp = s1.get()
            s2.put(temp)
            if temp.left_child:
                s1.get(temp.left_child)
            if temp.right_child:
                s1.get(temp.right_child)
        while not s2.empty():
            self._visit(s2.get())

    def level_order(self, root):
        q = Queue()
        q.put(root)
        while q.empty():

            temp = q.get()
            self._visit(temp)
            if temp.left_child:
                q.put(temp.left_child)
            if temp.right_child:
                q.put(temp.right_child)

    def insert_AVL(self, root: Node, data):
        if not root:
            self.size += 1
            return Node(data=data)
        if data < root.data:
            root.left_child = self.insert_AVL(root.left_child, data)
        else:
            root.right_child = self.insert_AVL(root.right_child, data)
        root.height = max(self.get_height(root.left_child), self.get_height(root.right_child)) + 1
        balance_factor = self._balance_factor(root)
        if balance_factor > 1 and self._balance_factor(root.left_child) >= 0:
            return self._right_rotate(root)
        if balance_factor < -1 and self._balance_factor(root.right_child) <= 0:
            return self._left_rotate(root)
        if balance_factor > 1 and self._balance_factor(root.left_child) < 0:
            root.left_child = self._left_rotate(root.left_child)
            return self._right_rotate(root)
        if balance_factor < -1 and self._balance_factor(root.right_child) > 0:
            root.right_child = self._right_rotate(root.right_child)
            return self._left_rotate(root)
        return root

    def insert(self, root: Node, data):
        if not root:
            root = Node(data=data)
        elif data < root.data:
            root.left_child = self.insert(root.left_child, data)
        else:
            root.right_child = self.insert(root.right_child, data)
        return root

    def insert_BST(self, data):
        n = Node(data=data)
        temp = self.root
        while temp:
            if data < temp.data:
                if not temp.left_child:
                    temp.left_child = n
                    return
                else:
                    temp = temp.left_child
            else:
                if not temp.right_child:
                    temp.right_child = n
                    return
                else:
                    temp = temp.right_child

    def min_node(self, root):
        temp = root
        while temp.left_child:
            temp = temp.left_child
        return temp

    def delete_AVL(self, root: Node, data):
        if not root:
            return None
        rtn = root
        if data < root.data:
            root.left_child = self.delete_AVL(root.left_child, data)
        elif data > root.data:
            root.right_child = self.delete_AVL(root.right_child, data)
        else:
            if not root.left_child:
                rtn = root.right_child
                root.right_child = None
                self.size -= 1
            elif not root.right_child:
                rtn = root.left_child
                root.left_child = None
                self.size -= 1
            else:
                temp = self.min_node(root.right_child)
                temp.right_child = root.right_child
                temp.left_child = root.left_child
                root.left_child = root.right_child = None
                rtn = temp

        rtn.height = max(self.get_height(rtn.left_child), self.get_height(rtn.right_child))
        balance_factor = self._balance_factor(rtn)
        if balance_factor > 1 and self._balance_factor(rtn.left_child) >= 0:
            return self._right_rotate(rtn)
        if balance_factor < -1 and self._balance_factor(rtn.right_child) <= 0:
            return self._left_rotate(rtn)
        if balance_factor > 1 and self._balance_factor(rtn.left_child) < 0:
            rtn.left_child = self._left_rotate(rtn.left_child)
            return self._right_rotate(rtn)
        if balance_factor < -1 and self._balance_factor(rtn.right_child) > 0:
            rtn.right_child = self._right_rotate(rtn.right_child)
            return self._left_rotate(rtn)
        return rtn

    def get_node_num(self, root):
        if not root:
            return 0
        else:
            return self.get_node_num(root.left_child) + self.get_node_num(root.right_child) + 1

    def getNodeNum(self, root):
        num = 0
        q = Queue()
        if root:
            q.put(root)
            num += 1
        while not q.empty():
            temp = q.get()
            if temp.left_child:
                q.put(temp.left_child)
                num += 1
            if temp.right_child:
                q.put(temp.right_child)
                num += 1
        return num

    def get_tree_height(self, root):
        if not root:
            return 0
        else:
            return max(self.get_tree_height(root.left_child), self.get_tree_height(root.right_child)) + 1
