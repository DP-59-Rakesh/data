'''-----------stack---------'''
class stack:
    def __init__(self):
        self.st=[]
    def push(self,data):
        self.st.append(data)
    def pop(self):
        if self.st==[]:
            print("stack is empty")
        else:
            return self.st.pop()
    def peek(self):
        if self.st==[]:
            print("stack is empty")
        else:
            return self.st[-1]
    def display(self):
        if self.st==[]:
            print("stack is empty") 
        else:
            return self.st
    def search(self,element):
        if self.st==[]:
            print("stack is empty")        
        else:
            n=self.st.index(element)
            return n
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(*s.display())
print(s.search(30))      





class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class stack:
  def __init__(self):
    self.head=None
  def push(self,data):
    newnode=node(data)
    newnode.next=self.head
    self.head=newnode
  def pop(self):
    self.head=self.head.next
  def display(self):
    current=self.head
    while current is not None:
      print(current.data,end=" ")
      current=current.next
x=list(map(int,input().split()))
k=stack()
for i in x:
  k.push(i)
k.display()
k.pop()
print()
print()
k.display()
print()
print(k.head.data)
                       



'''-------------queue--------------'''

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class queue():
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            self.head=self.head.next
    def peek(self):
        print(self.head.data)
        print(self.tail.data)
    def display(self):
        cur=self.head
        while cur is not None:
            print(cur.data,"->",end=" ")
            cur=cur.next      
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.peek()
q.display()                             