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

    def searchvalue(self, searchvalue):
        if searchvalue < 0:
            return "Invalid value. Please do not enter negative numbers"
        elif self.head is None:
            return "The list does not exist"
        else:
            searcher = self.head
            while searcher is not None:
                if searcher.value == searchvalue:
                    return searcher.value
                searcher = searcher.next
            return "The value does not exist in the list"






def main():

    list = SLinkedList()
    list.insertend(1)
    list.insertend(2)
    list.insertend(3)
    list.insertend(4)
    list.insertend(5)
    list.traversal()
    print("search value")
    print("------------")
    print(list.searchvalue(1))



main()