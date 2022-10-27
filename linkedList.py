class Node():
    
    # constructor
    def __init__(self, dataInput):
        self.data = dataInput

    def setNext(self, dataInput):
        self.next = Node(dataInput)

    def getNext(self):
        try:
            return self.next
        except Exception:
            return False


class LinkedList():

    # constructor
    def __init__(self, firstData):
        self.head = Node(firstData)
        
    # adds a node
    def append(self, dataInput):
        # set a pivot on the head
        current = self.head

        # loop until that pivot is the last node
        while (current.getNext()):
            current = current.getNext()

        # give that last node a child
        current.setNext(dataInput)

    # prints all values
    def printOut(self):
        current = self.head

        while (current.getNext()):
            print(current.data)
            current = current.getNext()
        print(current.data)



def main():
    list = LinkedList(0)
    for i in range(1,10):
        list.append(i)
    list.printOut()


if __name__ == "__main__":
    main()