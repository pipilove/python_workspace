#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pipi'
__mtime__ = '3/23/17'
__email__ = 'pipijob@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━┓┓┏━━┳┓┏━┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, xi):
        self.items.append(xi)

    def pop(self):
        if len(self.items) >= 1:
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0
        #     return self.size() == 0

    # def clear(self):
    #     del self.items[:]
    #     # self.items = []

    # def top(self):
    #     return self.items[self.size() - 1]

    def show(self):
        print([item.data for item in self.items])


class Queue():
    def __init__(self):
        self.items = []

    def push(self, xi):
        self.items.append(xi)

    def pop(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def empty(self):
        return len(self.items) == 0


class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        # self.parent = parent


class Tree():
    def __init__(self):
        self.root = None

    def insert(self, xi):
        now = self.root
        node = Node(xi, None, None)
        if now == None:
            self.root = node
        else:
            while now != None:
                now_parent = now
                if node.data <= now.data:
                    now = now.left
                else:
                    now = now.right
            if node.data <= now_parent.data:
                now_parent.left = node
            else:
                now_parent.right = node

    def build(self, x):
        for xi in x:
            self.insert(xi)

    def search(self, xi):
        '''
        二叉树非递归查找：节点存在则返回值为xi的节点的指针
        '''
        root = self.root

        while root and xi != root.data:
            if xi < root.data:
                root = root.left
            elif xi > root.data:
                root = root.right
        return root

    def delete(self, xi):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def successor(self):
        pass

    def draw(self):
        pass

    def preorder_travel_recursion(self, root):
        if root != None:
            print(root.data)  # print
            self.preorder_travel_recursion(root.left)  # 递归1
            self.preorder_travel_recursion(root.right)  # 递归2

    def preorder_travel(self):
        root = self.root
        s = Stack()
        result = []

        while root or not s.empty():
            while root:
                result.append(root.data)
                s.push(root)
                root = root.left
            root = s.pop()
            root = root.right

        # while robot or not s.empty():
        #     if robot:
        #         result.append(robot.data)
        #         s.push(robot)
        #         robot = robot.left
        #     else:
        #         robot = s.pop()
        #         robot = robot.right

        print('先序遍历：{}'.format(result))

    def inorder_travel_recursion(self, root):
        if root != None:
            self.inorder_travel_recursion(root.left)  # 递归1
            print(root.data)  # print
            self.inorder_travel_recursion(root.right)  # 递归2

    def inorder_travel(self):
        root = self.root
        s = Stack()
        result = []

        while root or not s.empty():
            while root:  # 递归1进入时压栈
                s.push(root)
                root = root.left
            # if not s.empty():
            root = s.pop()
            result.append(root.data)  # print
            root = root.right  # 递归2

        # while robot or not s.empty():
        #     if robot:  # 递归1进入时压栈
        #         s.push(robot)
        #         robot = robot.left
        #     else:
        #         robot = s.pop()
        #         result.append(robot.data)  # print
        #         robot = robot.right  # 递归2

        print('中序遍历：{}'.format(result))

    def postorder_travel_recursion(self, root):
        if root != None:
            self.postorder_travel_recursion(root.left)  # 递归1
            self.postorder_travel_recursion(root.right)  # 递归2
            print(root.data)  # print

    def postorder_travel(self):
        root = self.root
        s = Stack()
        result = []

        # while robot or not s.empty():
        #     while robot:
        #         s.push(robot)
        #         robot = robot.left
        #     robot = s.pop()
        #     s.push(robot)
        #     robot = robot.right
        #     while robot:
        #         s.push(robot)
        #         robot = robot.left
        #     robot = s.pop()
        #     s.push(robot)
        #     robot = robot.right
        # result.append(robot.data)
        # robot = None

        if root:
            s.push(root)
            while not s.empty():
                root = s.pop()
                # print数据前先记录左右两边的状态
                if root.left:
                    s.push(root.left)
                if root.right:
                    s.push(root.right)
                result.append(root.data)

            result = result[::-1]

        print('后序遍历：{}'.format(result))

    def bfs(self):
        root = self.root
        queue = Queue()
        result = []

        if root:
            queue.push(root)
            while not queue.empty():
                item = queue.pop()
                result.append(item.data)
                if item.left:
                    queue.push(item.left)
                if item.right:
                    queue.push(item.right)
        print('层次遍历：{}'.format(result))


def test():
    x = [4, 5, 1, 2, 3, 0, 3]
    x = [10, 5, 1, 8, 7, 9, 20, 15, 17]
    # x = []
    print(x)
    tree = Tree()
    tree.build(x)
    # tree.preorder_travel_recursion(tree.robot)
    tree.preorder_travel()
    # tree.inorder_travel_recursion(tree.robot)
    tree.inorder_travel()
    # tree.postorder_travel_recursion(tree.robot)
    tree.postorder_travel()
    tree.bfs()


if __name__ == '__main__':
    test()
