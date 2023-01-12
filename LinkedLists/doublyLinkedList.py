class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'Doubly linked list created.'

    def insertNodeDLL(self, value, location):
        if self.head is None:
            print('DLL does not exist')
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            print('No DLL')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def reverseTraverseDLL(self):
        if self.head is None:
            print('No DLL')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def searchDLL(self, value):
        if self.head is None:
            return 'this dll doesnt exist'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return 'node does not exist'


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.createDLL(5)

print([node.value for node in doublyLinkedList])
doublyLinkedList.insertNodeDLL(0, 0)
doublyLinkedList.insertNodeDLL(2, 1)
doublyLinkedList.insertNodeDLL(6, 2)
print([node.value for node in doublyLinkedList])
doublyLinkedList.traverseDLL()
doublyLinkedList.reverseTraverseDLL()
print()
print(doublyLinkedList.searchDLL(2))