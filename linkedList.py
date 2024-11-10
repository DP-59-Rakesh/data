class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class ll():
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        new_node=node(data)            
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data)    :
        new_node=node(data)
        cur=self.head 
        if self.head is None:
            self.head=new_node
        else:
            while cur.next is not None:
                cur=cur.next
        cur.next=new_node
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:    
            cur=self.head
            while cur is not None:
                print(cur.data,"-->",end=" ")
                cur=cur.next
    def add_before(self,data,x):
        new_node=node(data)
        if self.head is None:
            print("linked list is empty")
        if self.head==x:
            new_node.next=self.head
            self.head=new_node
        else:
            cur=self.head
            while cur.next is not None:
                if  cur.next.data==x:
                    break   
                cur=cur.next    
            new_node.next=cur.next
            cur.next=new_node
    def add_after(self,data,x):
        new_node=node(data)
        if self.head is None:
            print("linked list is empty")
        else:
            cur=self.head
            while cur.next is not None:
                if cur.data==x:
                    break 
                cur=cur.next  
            new_node.next=cur.next
            cur.next=new_node 
    def del_begin(self):
        if self.head is None:
            print("linked list is empty")
        else:
            self.head=self.head.next
    def del_end(self):
        if self.head is None:
            print('linked list is empty')
        elif self.head.next is None:
            self.head=None    
        else:
            cur=self.head
            while cur.next.next is not None:
                cur=cur.next                
            cur.next=None
    def del_at_node(self,x):
        if self.head is None:
            print("linked list is empty")
        elif self.head.data==x:
            self.head=None
        else:
            cur=self.head
            while cur.next is not None:
                if cur.next.data==x:
                    break
                cur=cur.next
            if cur.next is None:
                print('element not found')
            else:
                cur.next=cur.next.next 
    def mid(self):
        i=0
        f=self.head
        k=self.head
        while f.next is not None and f.next.next is not None:
            k=k.next
            f=f.next.next
            i+=1
        print(i)    
        print(k.data)  
        print(k.next.data) 
    def reverse(self):
        prev=None
        cur=self.head
        while cur is not None:
            f=cur.next
            cur.next=prev
            prev=cur
            cur=f                                     

l=ll()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)                        
l.add_end(20)
l.add_end(30)
l.add_end(40)
l.add_after(50,30)
# l.add_before(60,40)
l.del_at_node(70)
l.mid()
l.traversal()



'''-----------------Double linked list-----------------'''


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def add_before(self, data, x):
        if self.head is None:
            print("Doubly linked list is empty")
            return

        cur = self.head
        while cur and cur.data != x:
            cur = cur.next

        if cur is None:
            print("Element not found")
        else:
            new_node = DNode(data)
            new_node.next = cur
            new_node.prev = cur.prev
            if cur.prev:
                cur.prev.next = new_node
            else:
                self.head = new_node
            cur.prev = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("Doubly linked list is empty")
            return

        cur = self.head
        while cur and cur.data != x:
            cur = cur.next

        if cur is None:
            print("Element not found")
        else:
            new_node = DNode(data)
            new_node.prev = cur
            new_node.next = cur.next
            if cur.next:
                cur.next.prev = new_node
            cur.next = new_node

    def del_begin(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def del_end(self):
        if self.head is None:
            print("Doubly linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.prev.next = None

    def del_at_node(self, x):
        if self.head is None:
            print("Doubly linked list is empty")
        elif self.head.data == x:
            self.del_begin()
        else:
            cur = self.head
            while cur and cur.data != x:
                cur = cur.next
            if cur is None:
                print("Element not found")
            else:
                cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev

    def traversal(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            cur = self.head
            while cur:
                print(cur.data, "<-->", end=" ")
                cur = cur.next
            print("None")




'''---------------circular linked list---------------'''


class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def add_before(self, data, x):
        if self.head is None:
            print("Circular linked list is empty")
            return

        if self.head.data == x:
            self.add_begin(data)
            return

        new_node = CNode(data)
        cur = self.head
        while cur.next != self.head and cur.next.data != x:
            cur = cur.next

        if cur.next == self.head:
            print("Element not found")
        else:
            new_node.next = cur.next
            cur.next = new_node

    def add_after(self, data, x):
        if self.head is None:
            print("Circular linked list is empty")
            return

        cur = self.head
        while cur.next != self.head and cur.data != x:
            cur = cur.next

        if cur.data != x:
            print("Element not found")
        else:
            new_node = CNode(data)
            new_node.next = cur.next
            cur.next = new_node

    def del_begin(self):
        if self.head is None:
            print("Circular linked list is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("Circular linked list is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            cur = self.head
            while cur.next.next != self.head:
                cur = cur.next
            cur.next = self.head

    def del_at_node(self, x):
        if self.head is None:
            print("Circular linked list is empty")
            return

        if self.head.data == x:
            self.del_begin()
            return

        cur = self.head
        while cur.next != self.head and cur.next.data != x:
            cur = cur.next

        if cur.next == self.head:
            print("Element not found")
        else:
            cur.next = cur.next.next

    def traversal(self):
        if self.head is None:
            print("Circular linked list is empty")
        else:
            cur = self.head
            while True:
                print(cur.data, "-->", end=" ")
                cur = cur.next
                if cur == self.head:
                    break
            print("(head)")




'''------------------reversed of linked list---------------'''