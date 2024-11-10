class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst():
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(self.root,data)
    def _insert(self,current,data):
        if data<current.data:
            if current.left is None:
                current.left=node(data)
            else:
                self._insert(current.left,data) 
        elif data>current.data:
            if current.right is None:
                current.right=node(data)
            else:
                self._insert(current.right,data) 
    def search(self,data):
        return self._search(self.root,data)
    def _search(self,current,data):
        if current is None:
            print(False)
        if data==current.data:
            print(True)
        elif data<current.data:
            return self._search(current.left,data)
        else:
            return self._search(current.right,data)
    def delete(self,data):
        self.root=self._delete(self.root,data)
    def _delete(self,current,data):
        if current is None:
            return current     
        if data<current.data:
            current.left=self._delete(current.left,data)
        elif data>current.right:
            current.right=self._delete(current.right,data)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            min_val=self._min_val(current.right)
            current.data=min_val
            current.right=self._delete(current.right,min_val) 
        return current
    def _min_val(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current.data   
    def in_order(self):
        self._in_order(self.root)
        print()
    def _in_order(self,current):
        if current is not None :
            self._in_order(current.left)
            print(current.data,end=" ")
            self._in_order(current.right)                
    def pre_order(self):
        self._pre_order(self.root)
        print()
    def _pre_order(self,current):
            if current is not None:
                print(current.data, end=" ")
                self._pre_order(current.left)
                self._pre_order(current.right)
    def post_order(self):
        self._post_order(self.root)
        print()
    def _post_order(self, current):
        if current is not None:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.data, end=" ")

b=bst()
b.insert(50)
b.insert(70)
b.insert(60)
b.insert(20)
b.insert(40)
b.insert(30)
b.insert(80)
b.in_order()
b.pre_order()
b.post_order
b.search(60)
                        
