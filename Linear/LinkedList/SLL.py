#SinglyLinkedList
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
head=None
def insertBegin(data):
    global head
    if(head==None):
        head=node(data)
    else:
        newNode=node(data)
        newNode.next=head
        head=newNode
def insertEnd(data):
    global head
    if(head==None):
        head=node(data)
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=node(data)
def delEnd():
    global head
    if(head==None):
        pass
    else:
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        
def delBegin():
    global head
    if(head==None):
        pass
    else:
        temp=head.next
        del head
        head=temp
def showList():
    global head
    temp=head
    while(temp!=None):
        print(temp.data,end='->')
        temp=temp.next  
insertBegin(20)
insertBegin(30)
insertEnd(40)
insertEnd(46)
delEnd()
showList()
