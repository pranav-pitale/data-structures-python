
class BinarySearchtree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
    
    def _insert(self, node, root):
        if root == None:
            self.root = node
        else:
            if node.data <= root.data:
                if root.left == None:
                    root.left = node
                else:
                    self._insert(node,root.left)
            else:
                if root.right == None:
                    root.right = node
                else:
                    self._insert(node,root.right)

    def insert(self, data):
        temp = self.root
        node = self.Node(data)
        self._insert(node, temp)

    def _pre_order(self, root):
        if root:
            print(root.data)
            self._pre_order(root.left)
            self._pre_order(root.right)

    def pre_order(self):
        if self.root:
            self._pre_order(self.root)
 
    def _in_order(self,root):
        if root:
            self._in_order(root.left)
            print(root.data)
            self._in_order(root.right)

    def in_order(self):
        if self.root:
            self._in_order(self.root)

    def _post_order(self, root):
        if root:
            self._in_order(root.left)
            self._in_order(root.right)
            print(root.data)

    def post_order(self):
        if self.root:
            self._post_order(self.root)
    
    def _height(self,root):
        if root == None:
            return 0
        else:
            lheight = self._height(root.left)
            rheight = self._height(root.right)
            if (lheight > rheight):
                return lheight+1
            else:
              return rheight+1

    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return 0

    def height_iter(self):
        if self.root:
            temp = self.root
            lheight = 1
            rheight = 1
            
            while temp.left:
                lheight+=1
                temp = temp.left

            while temp.right:
                rheight+=1
                temp = temp.right
            return lheight if lheight > rheight  else rheight

    def level_order(self):

        if self.root:
            queue = list()
            queue.append(self.root)

            while len(queue) > 0 :
                temp = queue.pop()
                print(temp.data)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        else:
            return

    def reverse_level_order(self):

        if self.root:
            queue = list()
            stack = list()
            queue.append(self.root)

            while len(queue) > 0 :
                temp = queue.pop()
                stack.append(temp)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            while len(stack)>0:
                print(stack.pop().data)
        else:
            return


class driver:
    if __name__ == "__main__":
        obj = BinarySearchtree()
        obj.insert(2)
        obj.insert(1)
        obj.insert(3)
        obj.insert(5)

        obj.pre_order()
        print('=============')
        obj.in_order()
        print('=============')
        obj.post_order()
        print('=============')
        # print(obj.height())
        # print(obj.height_iter())
        obj.level_order()
        print('=============')
        obj.reverse_level_order()