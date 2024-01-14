class node:
    def __init__(self, data):
        self.prev=None
        self.data=data
        self.next=None     
head=None
def insertPrev(data):
    global head
    newNode=node(data)
    if(head==None):
        head=newNode
    else:
        temp=head
        while(temp.prev!=None):
            temp=temp.prev
        temp.prev=newNode
def insertNext(data):
    global head
    newNode=node(data)
    if(head==None):
        head=newNode
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=newNode
def delPrev():
    global head
    temp=head
    if(head==None):
        return
    while(temp.prev.prev!=None):
        temp=temp.prev
    temp.prev=None
def delEnd():
    global head
    temp=head
    if(head==None):
        return
    while(temp.next.next!=None):
        temp=temp.next
    temp.next=None
def showNexts():
    global head
    temp=head
    while (temp!=None):
        print(temp.data,end='->')
        temp=temp.next
    print()
def showPrevious():
    global head
    temp=head
    while(temp!=None):
        print(temp.data,end='<-')
        temp=temp.prev
    print()
    
insertNext(10)
insertNext(40)
insertPrev(20)

showNexts()
showPrevious()