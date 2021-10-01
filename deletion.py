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

    def deletefront(self):
        if self.head is None:
            return "The list is empty there is nothing to delete"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def deleteback(self):
        if self.head is None:
            return "The list is empty there is nothing to delete"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            seacher = self.head
            while seacher is not None and seacher.next is not  self.tail:
                seacher = seacher.next
            seacher.next = None
            self.tail = seacher
    def deletefromanylocation(self,location):
        if self.head is None:
            return "The list is empty there is nothing to delete"
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            front = self.head
            back = None
            counter = 0
            while front.next is not None and location > counter:
                counter +=1
                back = front
                front = front.next
            if back is not None:
                back.next = front.next
            else:
                self.head = front.next
                front = self.head
            if front.next is None:
                self.tail = back


def delvalidaton():
    location = int(input("Enter location:"))
    while location < 0:
        print("Invalid Number. Try again")
        location = int(input("Enter location:"))
    return location




def main():

    list = SLinkedList()
    list.insertend(1)
    list.insertend(2)
    list.insertend(3)
    list.insertend(4)
    list.insertend(5)
    list.insertend(6)
    list.insertend(7)
    list.insertend(8)
    list.traversal()
    print("Deleting front node")
    list.deletefront()
    list.traversal()
    print("Deleting back node")
    list.deleteback()
    list.traversal()
    print("Delete from any location")
    print("Enter location you want the node to be deleted")
    deletelocation = delvalidaton() #validation for nth location 
    list.deletefromanylocation(deletelocation)
    list.traversal()

main()