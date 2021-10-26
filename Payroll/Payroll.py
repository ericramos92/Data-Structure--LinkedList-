class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Slinkedlist:
    def __init__(self):
        self.head= None
        self.tail = None
        self.counter = 0
        self.checker = None
        self.id = None
    def append(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.checker =newnode
            self.tail = newnode
            self.id = newnode
            self.counter += 1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.counter += 1
    def printvalue(self):
        s = True
        while s:
            print(self.checker.value)
            self.checker = self.checker.next
            s = False
    def printvalueid(self):
        s = True
        while s:
            print(self.id.value)
            self.id = self.id.next
            s = False
    def wages(self,num):
        if num == 0:
            temp = self.head
            return temp.value
        elif num > 0:
            s = True
            while s:
                self.checker = self.checker.next
                s = False
                return self.checker.value
    def value(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



#validation
def validationhours():
    hours = int(input("Enter hour:"))
    while hours < 0:
        print("Please enter valid hours.")
        print("No negetaives number.")
        hours = int(input("Re-enter hour:"))
    return hours
def validationpayrate():
    pay = int(input("Enter Payrate:"))
    while pay < 0 or pay >15:
        print("Please enter valid payrate.")
        print("No negetaives number.")
        print("No payrate above 15 dollars")
        pay = int(input("Enter Payrate:"))
    return pay



def main():
    #ID
    id = Slinkedlist()
    id.append(5658845)
    id.append(4520125)
    id.append(7895122)
    #Hours
    hours = Slinkedlist()
    payrate = Slinkedlist()
    wage = Slinkedlist()
    for i in range(3):
        print("Employee")
        print("--------")
        id.printvalue()
        hour = validationhours()
        hours.append(hour)
        pay = validationpayrate()
        payrate.append(pay)
        w = hours.wages(i) * payrate.wages(i)
        wage.append(w)
    print("---------------------------")
    print("           Display ID's        ")
    print("---------------------------")
    id.value()
    print("---------hours-------------")
    hours.value()
    print("---------Payrate-------------")
    payrate.value()
    print("---------Wages-------------")
    wage.value()





main()