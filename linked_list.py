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
        node_to_insert = Node(data)
        if self.head == None:
            self.head = node_to_insert
        else: 
            node_to_insert.next = self.head
            self.head = node_to_insert
            
        return self.head
    
    def insert_in_between(self, data, position):
        self.node_position = 0 
        node_to_insert = Node(data)
        if self.head is None:
            self.head = node_to_insert
            #self.node_position += 1
            return self.head
            
        elif self.head is not None:
            current = self.head
            while current.next:
                if (self.node_position + 1) == position:
                    break
                else:
                    current = current.next
                    self.node_position += 1 
            
        store_next = current.next
        current.next = node_to_insert
        node_to_insert.next = store_next
        
        return self.head

    


    
    
