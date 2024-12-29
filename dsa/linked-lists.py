class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = Node(4)
node_b = Node(2)
node_c = Node(3)
tail = Node(10)

head.next = node_b
node_b.next = node_c
node_c.next = tail

def countNodes(head: Node) -> int:
    # assuming that head is not null
    count = 1
    current_node = head
    while current_node.next:
        count += 1
        current_node = current_node.next

    return count

print(countNodes(head))

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, value):
        new_value = Node(value)
        new_value.next = self.head

        self.head = new_value
        self.tail = self.tail if self.tail else new_value

        return self
    
    def append(self, value):
        new_value = Node(value)

        if self.head is None:
            # if there is no head, it does not exist, so the added node will be either the head and the tail
            self.head = new_value
            self.tail = new_value

            return
        
        # makes the tail point to the new added value
        self.tail.next = new_value
        # the new added value becomes the tail
        self.tail = new_value

    def traverse(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def find_value(self, value):
        current_node = self.head

        while current_node:
            if current_node.data == value:
                return current_node.data
            
            current_node = current_node.next

        return None
    
    def delete_head(self):
        if not self.head:
            return
        
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

    def to_array(self):
        array = []
        current_node = self.head

        while current_node:
            array.append(current_node.data)
            current_node = current_node.next

        return array

list = LinkedList()

list.prepend(2)
list.append(4)
list.prepend(1)
list.append(6)
list.prepend(10)
list.traverse()

list_as_array = list.to_array()
print(list_as_array)