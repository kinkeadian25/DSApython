class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def traverseSLL(self):
        if self.head is None:
            print('the SLL does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node=node.next

    def searchSLL(self, value):
        if self.head is None:
            print('the SLL does not exist')
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "value does not exist"

    def deleteNodeSLL(self, location):
        if self.head is None:
            print('the SLL does not exist')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    def deleteWholeSLL(self):
        if self.head is None:
            print('the sll does not exist')
        else:
            self.head=None
            self.tail=None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 2)
singlyLinkedList.insertSLL(4, 3)
singlyLinkedList.insertSLL(5, 4)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(5))
singlyLinkedList.deleteNodeSLL(4)
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteWholeSLL()
print([node.value for node in singlyLinkedList])



