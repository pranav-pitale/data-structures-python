
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def enqueue(self,data):
        node = self.Node(data)

        if(self.front):
            temp = self.front

            while(temp.next):
                temp = temp.next
            temp.next = node
            self.rear = node
        
        else:
            self.front = node
            self.rear = node
    
    def deque(self):
        if(self.front):
            if(self.front == self.rear):
                self.front = None
                self.rear = None
            else:
                temp = self.front

                while(temp.next.next):
                    temp = temp.next
                
                temp.next = None
                self.rear = temp
    
    def display(self):
        if(self.front):

            temp = self.front

            while(temp):
                print(temp.data)
                temp = temp.next


class driver:
    if __name__ == "__main__":
        obj = Queue()
        obj.enqueue(1)
        obj.enqueue(2)
        obj.enqueue(3)
        obj.display()
        print("============")
        obj.deque()
        obj.display()
