class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return 
        
        # add to left side of the tree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
                
        # add to right side of the tree
        else:
            if self.right:
                self.right.add_child(data)
            else: 
                self.right = BinarySearchTreeNode(data)
                
    # in order traversal
    def in_order_traversal(self):
        ordered = []
        # check and add left side of the tree
        if self.left:
            ordered += self.left.in_order_traversal()
        
        # add the current node
        ordered.append(self.data)
        
        # check and add right side of the tree
        if self.right:
            ordered += self.right.in_order_traversal()
            
        return ordered
    
    def search_value(self, value):
        if self.data == value: 
            return True
        
        elif value < self.data: 
            if self.left:
               return self.left.search_value(value)
            else:
                return False
        
        else: 
            if self.right:
                return self.right.search_value(value)
            else:
                return False
        
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
        
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
        
    def delete_value(self, value):
        if value < self.data: 
            if self.left:
               self.left = self.left.delete_value(value)
               return self
        
        elif value > self.data: 
            if self.right:
                self.right = self.right.delete_value(value)
                return self

        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            
            min_value = self.left.find_max()
            self.data = min_value
            self.left.delete_value(min_value)
            return self
            

    
def build_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root_node.add_child(elements[i])
        
    return root_node

elements = [12,53,54,13,64,84,38,23,90,23,11,8,34]
root_node = build_tree(elements)
print(root_node)
# print(root_node.delete_value(54))
print(root_node.in_order_traversal())
# print(root_node.search_value(84))


