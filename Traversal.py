class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # insert in Linked List
    def insertend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    #traversal
    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



def main():

    list = SLinkedList()
    list.insertend(2)
    list.insertend(3)

    list.traversal()

main()