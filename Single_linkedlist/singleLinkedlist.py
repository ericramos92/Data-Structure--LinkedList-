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
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                counter = 0
                temp_back = self.head
                while counter < location-1:
                    temp_back = temp_back.next
                    counter +=1
                #create new pointer
                temp_front = temp_back.next
                temp_back.next = newNode
                newNode.next =temp_front

    def showvalues(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
def main():

    list = SLinkedList()
    list.insertend(2)
    list.insertend(3)
    list.insertfront(1)
    print("Please enter location you wish to insert node")
    print ("-1 = at the end of LInked list \n 0 - At the front of Linklist")
    location = int(input("Enter your choice:"))
    value = int(input("Value:"))
    list.insertatlocation(value,location)
    list.showvalues()

main()


