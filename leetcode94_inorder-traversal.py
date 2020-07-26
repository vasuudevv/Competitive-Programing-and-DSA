class Node:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def preoder(root):

    list=[]
    current = root
   
    while True:

        if current is not None:
            # print(current.data)   PRINT PREORDER
            list.append(current)
            current = current.left
        elif(list):
            
            current = list.pop()
            print(current.data)
            current = current.right
            
        else:
            break
    
root = Node(1)
root.left= Node(2)
root.right= Node(3)
root.left.left= Node(4)
root.left.right= Node(5)

preoder(root)