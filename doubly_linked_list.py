class doubly_linked_list:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
    
    def append(self, data):

        node = self.Node(data)
        if(self.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node
            node.previous = temp
        else:
            self.head = node
    
    def push(self, data):

        node = self.Node(data)
        if(self.head):
            temp = self.head
            self.head = node
            self.head.next = temp
            temp.previous = self.head
        else:
            self.head = node

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def pop(self):

        if(self.head):
            temp = self.head

            if(temp.next):
                self.head = temp.next
                self.head.previous = None
            else:
                self.head = None

    def is_empty(self):

        if(self.head):
            return False
        else:
            return True

class driver:

    if __name__ == "__main__":
        obj = doubly_linked_list()
        obj.push(1)
        obj.push(2)
        obj.push(3)
        obj.display()
        print('--------------------------------')
        obj.append(4)
        obj.append(5)
        obj.display()