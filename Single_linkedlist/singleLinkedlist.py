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

    def insertfront(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertatlocation(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.front = self.head
            self.behind = None
            counter = 0

            while self.front is not None and location > counter:
                counter +=1
                self.behind = self.front
                self.front = self.front.next
            if self.behind is not None:
                newNode.next = self.behind.next
                self.behind.next= newNode
            else:
                newNode.next  = self.head
                self.head = newNode
            if self.front is None:
                self.tail = newNode


    def showvalues(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
def main():

    list = SLinkedList()
    list.insertend(0)
    list.insertend(1)
    list.insertend(2)
    list.insertend(3)
    list.insertend(4)


    location = int(input("Enter your choice:"))
    value = int(input("Value:"))
    list.insertatlocation(value,location)
    list.showvalues()

main()


