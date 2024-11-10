class node():
    def __init__(self):
        self.children={}
        self.end_of_word=False
class trie():
    def __init__(self):
        self.root=node()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=node()
            cur=cur.children[char]
        cur.end_of_word=True
    def search(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char] 
        return cur.end_of_word
    def starts_with(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char] 
        return True               
    

t=trie()
t.insert("apple")
print(t.search("apple"))
print(t.search("appl"))   
print(t.starts_with("appl"))  