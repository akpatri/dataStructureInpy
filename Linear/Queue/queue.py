queue=[]
def enqueue(data):
    queue.insert(0,data)
def dequeue():
    if(len(queue)!=0):
        queue.pop()
