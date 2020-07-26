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

    def detect(self):

        # curr = self.head                            # O(n) time  
        # s = set()                                   # O(n) space (because of hash set)
        # while(curr != None):
        #     if curr in s:
        #         return True
            
        #     s.add(curr)
        #     curr = curr.next
        # return False

        slow = self.head                                # O(n) time
        fast = self.head                                # O(1) space 
        while(slow and fast and fast.next):

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

ll = llist()

ll.head = node(1)
ll.head.next = node(2)
ll.head.next.next = node(3)
ll.addNode(4)

print(ll.detect())

