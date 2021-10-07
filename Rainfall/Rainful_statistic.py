class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def totalrainfall(self,total_months):
        temp = self.head
        counter = 0
        while temp is not None and counter < total_months:
            self.total += temp.value
            temp =temp.next
        return self.total
    def averagemonthly(self,total_months):
        average = 0.0
        average += self.total / total_months
        return average
    def highest(self):
        temp = self.head
        highest = 0
        while temp is not None:
            highest = max(highest ,temp.value)
            temp = temp.next
        return highest
    def lowest(self):
        temp = self.head
        min = self.head.value
        while temp is not None:
            if temp.value < min:
                min = temp.value
            temp =temp.next
        return min


    def showvalues(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
#validation
def validation():
    number = int(input("Enter Total of Months:"))
    while number < 0 or number > 12:
        print("Invalid numver. Please re-enter number from 1- 12")
        number = int(input("Enter Total of Months"))
    return number
def main():
    months= ["January","February","March","April","May","June","July","August","Setember","October","November","december"]
    rain = SLinkedList() # object
    totalmonths = validation()
    for i in range(totalmonths):
        rain_monthly =int(input("Enter the total rainfal for " + months[i] +":"))
        rain.append(rain_monthly)
    print("        Results        ")
    print("-----------------------")
    print("Total rainFall is "+str(rain.totalrainfall(totalmonths)))
    print("Total Average Monthly rainfall is " + str(rain.averagemonthly(totalmonths)))
    print("Highest rainFall is " + str(rain.highest()))
    print("Lowest rainFall is " + str(rain.lowest()))
main()