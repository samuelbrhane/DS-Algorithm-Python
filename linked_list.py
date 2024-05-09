class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # insert new item at the end linked list
    def insert_at_tail(self, item):
        linked_list_node = LinkedListNode(item)
        if self.head is None:
            self.head = linked_list_node
            
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = linked_list_node
                break
            current_node = current_node.next_node
      
    # insert new item at the start of linked list
    def insert_at_head(self, item):
        linked_list_node = LinkedListNode(item)
        if self.head is None:
            self.head = linked_list_node
            return
        
        head_node = self.head
        linked_list_node.next_node = head_node
        self.head = linked_list_node
        
    # insert new item after given node
    def insert_after_node(self, prev_node, item):
        if not prev_node:
            return "Previous node not found"
        linked_list_node = LinkedListNode(item)
        linked_list_node.next_node = prev_node.next_node
        prev_node.next_node = linked_list_node
      
        
    # find node from the linked list
    def find_node(self, item):
        current_node = self.head
        while current_node:
            if current_node.value == item:
                return current_node
            current_node = current_node.next_node
        return None
    
    
    # find previous node
    def find_prev_node(self, node):
        current_node = self.head
        while current_node.next_node:
            if current_node.next_node == node:
                return current_node
            current_node = current_node.next_node
        return None
    
    
    # delete item from the linked list
    def remove_node(self, node):
        if not node:
            return "Node not found"
        
        if node == self.head:
            self.head = node.next_node
            return 
        

        prev_node = self.find_prev_node(node)
        if prev_node is None:
            return "Node not found"
        prev_node.next_node = node.next_node
                

    # print items from the linked list
    def print(self):
        current_node = self.head
        
        while current_node:
            print(current_node.value, end="-->")
            current_node = current_node.next_node
        print("None")
        

linked_list = LinkedList()
linked_list.insert_at_head(2)
linked_list.insert_at_head(5)
linked_list.insert_at_head(6)
linked_list.insert_at_head(8)
linked_list.insert_at_tail(10)
prev_node = linked_list.find_node(6)
print(prev_node.next_node)
linked_list.insert_after_node(prev_node, 7)
linked_list.remove_node(prev_node)
linked_list.print()
                
        
            
