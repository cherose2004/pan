'''
约瑟夫环是一个经常出现在计算机科学和数学中的问题，并不难，题目的变化形式很多，求解的方法也很多.比如，用约瑟夫环解决报数的问题：有n个人围成一圈，顺序排号。从第一个人从1到3开始报数，报到3的人退出，问最后留下的是最初的几号？请用Python3编写程序解决这个问题。
当k是1的时候，存活的是最后一个人，当k>=2的时候，构造一个n个元素的循环链表，然后依次杀掉第k个人，留下的最后一个是可以存活的人。代码如下：
'''

class Node():
    def __init__(self,val = None,nt = None):
        self.value = val
        self.next = nt


#循环链表实现        
class CircularList(object):
    def __init__(self):
        self.headNode = Node()
        self.headNode.next = self.headNode
        self.head  = self.headNode
        self.curNode = self.headNode
        self.size = 0
    
    def __len__(self):
        return self.size

    def addElement(self,value):
        if self.size == 0:
            elementNode = Node(value)
            self.headNode = elementNode
            self.curNode = self.headNode
            self.size += 1
        else:
            elementNode = Node(value)
            self.curNode.next = elementNode
            elementNode.next = self.headNode
            self.curNode = elementNode
            # print("elem:",elementNode,"headnode:", self.headNode,"curnode:", self.curNode)
            self.size += 1

    def Joseph(self,num,count):
        if self.size <= count:
            return 'empty'
        
        currentNode = self.headNode
        i = 2
        while self.size > 1: 
            if i % count == 0:
                print(i,currentNode.next.value,"killed")
                currentNode.next = currentNode.next.next
                self.size -= 1
                i+=1
                continue
            i+=1
            currentNode = currentNode.next
        
        
        head_node = currentNode
        while True:
            print(currentNode.value)
            currentNode = currentNode.next
            if currentNode == head_node:
                break

        return


num = 1410
count = 3
cl = CircularList()
for i in range(1,num+1):
    cl.addElement(i)
cl.Joseph(num,count)




