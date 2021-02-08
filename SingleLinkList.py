# 节点的定义封装
class Node:
    def __init__(self,value=None,next_=None):
        self.value = value
        self.next_ = next_

    def getData(self):
        return self.value

    def getNext(self):
        return self.next_

    def setData(self,newdata):
        self.value = newdata

    def setNext(self,newnext):
        self.next_ = newnext

# 实现对链表的模拟有两种方法 list方法封装成链表方法 或者基于指针完成
class SLinklist1(object):
    def __init__(self,head=None):
        # head是node类型
        self.head = head
        self.items = []
        self.length = len(self.items)

    def isEmpty(self):
        return self.items == []

    def tailInsert(self,node):
        self.items.append(node.value)

    def headInsert(self,node):
        temp = self.head
        self.head = node
        self.head.next_ = temp

    def midInsert(self,node,index):



    def travel(self):
        for i in self.items:
            pass

    def reverse(self):
        return self.items.reverse()

node4 = Node('Thu')
node3 = Node('Wen',node4)
node2 = Node('Tue',node3)
node1 = Node('Mon',node2)

class SLinklist2(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getLength(self):
        l = 0
        cur = self.head
        while cur:
            cur = cur.next_
            l+=1
        return l

    def travel(self):
        cur = self.head
        while cur:
            print(cur.getData())
            cur = cur.next_

    def appendleft(self,node):
        if not self.head.next_:
            self.head = node
        node.next_ = self.head
        self.head = node

    def append(self,node):
        cur = self.head
        while cur.next_:
            cur = cur.next_
        cur.next_ = node
        node.next_ = None

    def midInsert(self,index,node):
        pass