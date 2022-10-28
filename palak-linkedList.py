class Node():
    # runs on startup
    def __init__(self, dataPassedIn):
        self.data = dataPassedIn

    # only gets run when you call it
    def setNextNode(self, node):
        self.nextNode = node

    def getNextNode(self):
        try:
            return self.nextNode
        except AttributeError:
            return False

class LinkedList():

    # constructor
    def __init__(self, initData):
        self.head = Node(initData)

    def append(self, passedData):
        current = self.head
        while (current.getNextNode()):
            current = current.getNextNode()

        # we can assume 'current' now points to the last node
        current.setNextNode(Node(passedData))

    def length(self):
        current = self.head
        count = 1
        while (current.getNextNode()):
            count += 1
            current = current.getNextNode()

        return count


def main():
    pass

if __name__ == "__main__":
    main()