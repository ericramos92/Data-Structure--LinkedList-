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

    def showvalues(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def search_position_of_value(self,value):

        searcher = self.head
        counter = 0

        while searcher is not None:
            if searcher.value != value:
                searcher =searcher.next
                counter+=1
            else:
                return counter
            if searcher.next is None and searcher.value != value:
                return -1
def main():

    list = SLinkedList()
    list.insertend(0)
    list.insertend(1)
    list.insertend(2)
    list.insertend(3)
    list.insertend(4)
    value =int(input("Enter the value:"))
    l =list.search_position_of_value(value)
    print("----------------")
    print("The position of the value is " + str(l))




main()



