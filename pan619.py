
# 魔术师利用一副牌中的13张黑桃，预先将它们排好后叠在一起，并使牌面朝下。然后他对观众说：“我不看牌，只要数数就可以猜到每张牌是什么，我大声数数，你们听，不信？你们就看。” 魔术师将最上面的那张牌数为1，把它翻过来正好是黑桃A，他将黑桃A放在桌子上，然后按顺序从上到下数手中的余牌，第二次数1、2，将第一张牌放在这迭牌的下面，将第二张牌翻过来，正好是黑桃2，也将它放在桌子上，第三次数1、2、3，将前面两张依次放在这迭牌的下面，再翻第三张牌正好是黑桃3，这样依次进行，将13张牌全部翻出来，准确无误。请用Python语言编程计算出魔术师手中的牌原始次序是怎样安排的？
# 假设桌子上有13个空盒子排成一圈，设定其中一个盒子序号为1，将黑桃A放入1号盒子中，接着从下一个空盒子开始重新计数，当数到第2个空盒子时，将黑桃2放入其中。然后再从下一个空盒子开始重新计数，数到第3个空盒子时，将黑桃3放入其中，这样依次进行下去，直到将13张牌全部放入空盒子中为止。需要注意的是，在计数过程中要跳过那些已放入牌的盒子，而只对空盒子计数。最后牌在盒子中的顺序，就是魔术师手中牌的顺序。


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
    
cl = CircularList()
cl.addElement(1)
for i in range(12):
    cl.addElement(0)

currentNode = cl.headNode
for j in range(2,14):
    count = 0
    while count < j :
        currentNode = currentNode.next
        if currentNode.value == 0:
            count += 1
        # print("count: ",count)
    currentNode.value = j

    


currentNode = cl.headNode
count = 1
while True and count < 14:
    print(currentNode.value)
    currentNode = currentNode.next
    count += 1