class node:
    def __init__(self, data):
        self.lchild=None
        self.data=data
        self.rchild=None
root=None
def insertNode(root,data):
    if(root==None):
        root=node(data)
    elif(data>root.data):
        root.rchild=insertNode(root.rchild,data)
    elif(data<root.data):
        root.lchild=insertNode(root.lchild,data)
    return root
def preOrder(root):
    if(root!=None):
        print(root.data,end='->')
        preOrder(root.lchild)
        preOrder(root.rchild)
        
def postOrder(root):
    if(root!=None):
        postOrder(root.rchild)
        postOrder(root.lchild)
        print(root.data,end='->')

def inOrder(root):
    if(root!=None):
        inOrder(root.lchild)
        print(root.data,end='->')
        inOrder(root.rchild)

def height(root):
    if(root==None):
        return -1
    else:
        return 1+max(height(root.lchild),height(root.rchild))

root=insertNode(root,5)
root=insertNode(root,3)
root=insertNode(root,2)    
inOrder(root)
