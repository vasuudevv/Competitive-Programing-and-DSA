class node:

    def __init__(self,data):

        self.data = data
        self.next = None
        

class llist:

    def __init__(self):
        self.head = None

    def addNode(self,newdata):
        curr = self.head
        while(curr.next != None):
            curr= curr.next

        new = node(newdata)
        curr.next = new
        new.next = None

    def deleteNode(self,value):
        temp = self.head
        curr = self.head

        if(curr.data == value):
            self.head = curr.next
            curr = None
            return
        curr = curr.next

        while(curr.data != value):
            curr = curr.next
            temp = temp.next

        temp.next = curr.next

    def insertBeg(self,value):
        curr = node(None)
        curr.data = value
        curr.next = self.head
        self.head = curr 


    def print(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next



ll = llist()

ll.head = node(1)
ll.head.next = node(2)
ll.head.next.next = node(3)

ll.addNode(4)
ll.print()
print("***")
#ll.deleteNode(1)
ll.insertBeg(0)
ll.print()
    


    







    