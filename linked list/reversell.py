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

    def print(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next

    def reverse(self):

        curr = self.head
        prev = None

        while(curr != None):

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
            
           



ll = llist()

ll.head = node(1)
ll.head.next = node(2)
ll.head.next.next = node(3)

ll.addNode(4)
ll.print()
print("***")
ll.addNode(5)
ll.reverse()
ll.print()

