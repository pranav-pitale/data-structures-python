class LinkedList:
    class Node:
        def __init__(self,dataIn):
            self.data = dataIn
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        node = self.Node(data)
        if(self.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
        else:
            self.head = node

    def push(self, data):
        node = self.Node(data)
        if(self.head):
            temp = self.head
            self.head = node
            self.head.next = temp
        else:
            self.head = node

    def pop(self):
        if(self.head):
            self.head = self.head.next

    def display(self):
        if(self.head):
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

    def reverse(self):
        if(self.head):
            reverse_list = LinkedList()
            temp = self.head

            while(temp):
                reverse_list.push(temp.data)
                temp = temp.next
            return reverse_list

    def join(self, llist):
        if(self.head and llist.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = llist.head

    def is_empty(self):
        if(self.head):
            return False
        else:
            return True
    
    def remove(self, position = None):
        cnt = 0

        if(position!= None):

            if(position == 0):

                self.pop()
            else:
                if(self.head):
                    temp = self.head

                    while(temp and cnt < position-1):
                        temp = temp.next
                        cnt+=1
                    if(temp):
                        temp.next = temp.next.next
        else:
            if(self.head):
                temp = self.head

                while(temp.next.next):
                    temp = temp.next
                
                temp.next = None

class Driver:
    
    if __name__ == "__main__":

        llist=LinkedList()
        llist.append(1)
        llist.append('8')
        llist.push(9)
        llist.append(3)
        llist.display()
        llist.pop()
        print("============")
        llist.display()
        llist.pop()
        print("============")
        llist.display()
        print("============")
        llist = llist.reverse()
        llist.display()
        print("============")
        llist1 = LinkedList()
        llist1.push(100)
        llist.join(llist1)
        llist.display()
        print("============")
        llist.remove(1)
        llist.display()
