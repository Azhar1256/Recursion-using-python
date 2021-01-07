class Node:

    def __init__(self,value,next):
        self.value = value
        self.next = next


    def printNode(self):
        print(self.value, '-', self.next)


class MyList:

    
    def __init__(self, a=None):
        if a == None:
            self.size = 0
            self.head = None
            self.tail = None

            
            
        elif isinstance(a, list):
            self.size = 0
            self.head = None
            self.tail = None
            for i in a:  # "a" is an array
                newNode = Node(i, None)
                if self.head == None:
                    self.head = newNode
                    self.tail = newNode
                    self.size += 1
                else:
                    self.tail.next = newNode
                    self.tail = newNode
                    self.size += 1


                    
                    
        elif isinstance(a, object):
            #self.size = 0
            self.head = None
            newTail = None
            node = a.head
            while node is not None:
                newNode = Node(node.value, None)
                if self.head == None:
                    self.head = newNode
                    newTail = newNode
                else:
                    newTail.next = newNode
                    newTail = newNode
                node = node.next

                
                
    def showList(self):
        n = self.head
        count = 0
        while (n != None):
            count += 1
            n = n.next

        if (count == 0):
            print("Empty List")
        else:
            n = self.head
            while (n != None):
                print(n.value,end=' ')
                n = n.next
                
                

    def sum_rec(self, node): 
        if node==None: 
            return 0
         
        return node.value + self.sum_rec(node.next)
    


list1=MyList([1,2,3,4,5,6])
list1.showList()
print()
a=list1.sum_rec(list1.head)
print(a)
list1.print_rev(list1.head)
