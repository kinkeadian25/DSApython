class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node

    def instertCicrularSLL(self, newValue, location):
        if self.head is None:
            return "the head ref. is None"
        else:
            newNode = Node(newValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            
            return 'node inserted'
        
    def traverseCSLL(self):
        if self.head is None:
            return 'linked list does not exist'
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break
    
    def searchCSLL(self, value):
        if self.head is None:
            print('the CSLL does not exist')
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
                if node == self.tail.next:
                    return "value does not exist"

    def deleteNodeCSLL(self, location):
        if self.head is None:
            print('the CSLL does not exist')
        if location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index+=1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    def deleteWholeCSLL(self):
        if self.head is None:
            return 'CSLL does not exist'
        else:
            self.head = None
            self.tail = None

circularSLL = CircularSLL()
circularSLL.createCSLL(1)
circularSLL.instertCicrularSLL(0,0)
circularSLL.instertCicrularSLL(1,1)
circularSLL.instertCicrularSLL(2,2)
circularSLL.instertCicrularSLL(3,3)
circularSLL.instertCicrularSLL(4,-1)

print([node.value for node in circularSLL])
circularSLL.traverseCSLL()
print(circularSLL.searchCSLL(6))
circularSLL.deleteNodeCSLL(1)
print([node.value for node in circularSLL])
circularSLL.deleteWholeCSLL()
print([node.value for node in circularSLL])