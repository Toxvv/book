class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        # 更改新节点的下一个引用以引用旧链表的第一个节点
        temp.setNext(self.head)
        # 赋值语句设置列表的头
        self.head = temp
        # 访问和赋值的顺序不能颠倒，因为head是链表节点唯一的外部引用，颠倒将导致所有原始节点丢失并且不能再被访问

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            # previous 必须先将一个节点移动到 current 的位置。此时，才可以移动current
            else:
                previous = current
                current = current.getNext()
        # 如果要删除的项目恰好是链表中的第一个项，链表的 head 需要改变
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist=UnorderedList()
mylist.add(31)
mylist.add(88)
print(mylist.search(2))