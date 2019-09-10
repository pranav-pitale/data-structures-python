class stack:
    class Node:
        def __init__(self,dataIn):
            self.data = dataIn
            self.next = None
    def __init__(self):
        self.top = None

    def push(self,value):
        node = self.Node(value)

        if(self.top == None):
            self.top = node
        else:
            temp = self.top
            self.top = node
            self.top.next = temp

    def peek(self):
        if(self.top):
            return self.top.data
        else:
            return None

    def pop(self):
        if(self.top):
            if(self.top.next):
                self.top = self.top.next
            else:
                self.top = None

    def display(self):
        temp = self.top
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def is_empty(self):
        if(self.top):
            return False
        else:
            return True

class Driver:
    if __name__ == "__main__":
        obj = stack()
        obj.push(1)
        obj.push(2)
        obj.push(3)
        obj.display()
        obj.pop()
        obj.display()
        obj.peek()
