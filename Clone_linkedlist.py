class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Helper function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data)
        print ("|")
        ptr = ptr.next
    print("None")



# Function takes a linked list and returns a complete copy of that
# list using a dummy node
def copyList(head):
    current = head  # used to iterate over the original list
    dummy = Node()  # build the new list of this dummy node

    # point to the last node in a new list
    tail = dummy  # start the tail pointing at the dummy

    while current:
        tail.next = Node(current.data, tail.next)  # add each node at the tail
        tail = tail.next  # advance the tail to the new last node
        current = current.next

    return dummy.next


if __name__ == '__main__':

    # construct a linked list
    head = None
    for i in reversed(range(4)):
        head = Node(i + 1, head)

    # copy linked list
    dup = copyList(head)

    # print duplicate linked list
    printList(dup)