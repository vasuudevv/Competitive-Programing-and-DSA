class node:

    def __init__(self,data):

        self.data = data
        self.next = None
        self.prev = None
        
class llist:

    def __init__(self):
        self.head = None

    def addNode(self,newdata):
        curr = self.head
        while(curr.next != None):
            curr= curr.next

        new = node(newdata)
        curr.next = new
        new.prev = curr
        new.next = None

    def deleteNode(self,value):
        temp = self.head
        curr = self.head

        if(curr.data == value):
            self.head = curr.next
            curr.next.prev = None
            curr = None
            return
        curr = curr.next

        while(curr.data != value):
            curr = curr.next
            temp = temp.next

        temp.next = curr.next
        curr.next.prev = temp

    def insertBeg(self,value):
        curr = node(None)
        curr.data = value
        curr.next = self.head
        curr.prev = None
        self.head.prev = curr 
        self.head = curr


    def print(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next

    def printRev(self):
        curr = self.head
        while(curr.next != None):
            curr = curr.next

        while(curr != None):
            print(curr.data)
            curr = curr.prev




ll = llist()

ll.head = node(1)

ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.printRev()
print("***")
ll.deleteNode(1)
ll.insertBeg(0)
ll.printRev()
    


    







    