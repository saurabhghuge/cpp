class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self):
        self.start = None
    def insertatend(self,value):
        #creating new node obeject 
        new_node = node(value)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    def delete(self, value ):
        if  self.start == None :
            print("list id empty")
        elif  self.start == value:
            temp = self.start
            self.start = self.start.next
        else:
            temp = self.start
            while temp.next.data != value:
                temp = temp.next
            prev = temp
            temp = temp.next
            prev.next = temp.next
    def viewlist(self):
        if self.start == None:

                print('list is empty')
        else :
            temp = self.start
            while temp != None:
                print(temp.data, end = " ") 
                temp = temp.next
        #print()
if __name__ == "__main__":
    list = linklist()
    list.insertatend(2)
    list.insertatend(4)
    list.insertatend(5)
    list.viewlist()
    list.delete(4)
    list.viewlist()

        

                        
