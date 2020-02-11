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
    def insert_at_start(self, data):
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

    def insert_at_end(self, data):    
        node_to_insert = Node(data)
        if(self.head is None):
            self.head = node_to_insert

        elif(self.head is not None):
            current = self.head
            while current.next:
                current = current.next
                
            current.next = node_to_insert
        return self.head

    def print_list(self):
        if self.head == None:
            return 
        else: 
            temp = self.head
            while temp is not None:
                print(temp.data, end = " -> ")
                temp = temp.next

    def reverse_ll(self):
        current = self.head
        prev_node = None

        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        self.head = prev_node
        return self.head
    
    def check_palindrome(self):
        """
        1. Split the linked list in middle
        2. Prepare two linked lists.
        3. If odd, ignore the middle node 
        4. Reverse the second linked list
        5. Compare the two linked lists
        """
        ## Splitting of Linked list
        p = self.head
        q = self.head
        while(p):
            p = p.next.next
            #to check linked list is odd
            if p.next is None:
                second_list = q.next.next 
                break
            elif p is None: # to check linked list is even
                second_list = q.next
                break
            q = q.next
        q.next = None

        # Reversing second list
        prev_node = None
        while(second_list):
            next_ref = second_list.next 
            second_list.next = prev_node
            prev_node = second_list
            second_list = next_ref
        second_list = prev_node

        
        
        

        


if __name__ == "__main__":

    print("LINKED  LIST...")
    ll = Linkedlist()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(20)
    ll.insert_at_end(10)
    ll.insert_at_start(250)
    ll.insert_in_between(880, 4)
    ll.print_list()  # O/P :-- 250 -> 10 -> 20 -> 30 -> 800 -> 20 -> 10 
    ll.reverse_ll()
    print("\nREVERSED  :\n")
    ll.print_list() # O/P after reversing :-- 10 -> 20 -> 880 -> 30 -> 20 -> 10 -> 250 -> 

 