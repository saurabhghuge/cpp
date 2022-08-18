class node:
    def __init__(self,data,pri):
        self.data = data
        self.pri = pri
        self.next = None
class priority:
    def __init__ (self):
        self.head = None
    
    def push(self,data,pri):
        new = node(data,pri)
        if self.head == None or new.pri < self.head.pri:
           new.next = self.head
           self.head = new

        else :
            temp = self.head
            while temp.next != None and temp.next.pri <= new.pri:
                temp = temp.next
            new.next = temp.next
            temp.next = new
        #que.view()
    def pop(self):
        temp = self.head
        if temp == None :
            print ("queue is empty")
        else :
            self.head = temp.next
            print(f"{temp.data}-> {temp.pri}  Rempved ",end="   ")
            print()
    def view(self):
        if self.head == None:
            print("queue is empty")
        else :
            temp = self.head
            while temp != None:
                print(f"{temp.data}-> {temp.pri}",end="   ")
                
                temp = temp.next
            print()


if __name__ == "__main__":
    que =  priority()
    que.push(8,2)
    que.push(7,4)
    que.push(9,3)
    que.view()    
    que.pop()
    que.view()

