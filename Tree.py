class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        parent = self.parent
        
        while parent is not None:
            level += 1
            parent = parent.parent
        
        return level
        
    def print_tree(self):
        prefix_space = " " * self.get_level() * 4
        print(prefix_space + str(self.get_level()) + "|__" + self.data)
        for child in self.children:
            child.print_tree()
        

def create_tree():
    root = TreeNode("Student")
    
    name = TreeNode("Name")
    name.add_child(TreeNode("First Name"))
    name.add_child(TreeNode("Last Name"))
    
    course = TreeNode("Course")
    course.add_child(TreeNode("Physic"))
    course.add_child(TreeNode("Chemistry"))
    course.add_child(TreeNode("Biology"))
    
    root.add_child(name)
    root.add_child(course)
    
    return root

root = create_tree()
root.print_tree()
    
    
    
    
        