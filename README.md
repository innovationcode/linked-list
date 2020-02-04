# linked-list
### A linked list is a linear data structure where each element is a separate object.
- Linked list elements are not stored at contiguous location; the elements are linked using pointers.

- Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

- In order to get to the end of the list, we have to go through all of the items in the list in order, or sequentially.
- The biggest differentiator between arrays and linked lists is the way that they use memory in our machines.
   - Arrays need a contiguous block of memory where as
   - Linked lists don't need to be contiguous in memory, they can grow dynamically.


## List types
#### Singly linked list : 
- Singly linked lists are the simplest type of linked list, based solely on the fact that they only go in one direction. There is a single track that we can traverse the list in; we start at the head node, and traverse from the root until the last node, which will end at an empty null value.
#### Doubly linked list : 
-  There are two references contained within each node: a reference to the next node, as well as the previous node. This can be helpful if we wanted to be able to traverse our data structure not just in a single track or direction, but also backwards, too.
#### circular linked list : 
- linked list where all nodes are connected to form a circle. There is no NULL at the end. A circular linked list can be a singly circular linked list or doubly circular linked list. 

## Big O Notation 😄 
- Inserting at start O(1)
- Inserting at end O(n)

# A linked list is usually efficient when it comes to adding and removing most elements, but can be very slow to search and find a single element.



