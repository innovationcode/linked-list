# Linked list is a collection of nodes .. We need node (structure with data and pointer to next)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Using above Node object construct Linked list
class Linkedlist:
    # linked list will have head by default so its in __init__
    # if list empty self.head = null 
    def __init__(self):
        self.head = None

    # We can insert a node in linked list in three ways
    # 1. Insert at start O(1)
    # 2. Insert at some position
    # 3. Inset at the end O(n)
    def insert_at_start(data):
        new_node_to_insert = Node(data)
        if self.head == None:
            self.head = new_node_to_insert
        else: 
            new_node_to_insert.next = head
            self.head = new_node_to_insert
            
        return self.head
    
    

    
    
