class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next= next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        if self.head is None:
            self.head = node
            return
        
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, current_node, None)
        

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count+=1
            current_node = current_node.next

        return count
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                new_node = Node(data, current_node, current_node.next)
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                break

            count += 1
            current_node = current_node.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        current_node = self.head
        while current_node:
            if count == index:
                current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                break

            count += 1
            current_node = current_node.next

    def print_forward(self):
        if self.head is None:
            print('Double Linked list is empty')
            return
        
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def print_backward(self):
        if self.head is None:
            print('Double Linked list is empty')
            return
        
        # while current_node.next:
        #     current_node = current_node.next # or create a function to do this part and return last node
        current_node = self.get_last_node()
        
        while current_node:
            print(current_node.data)
            current_node = current_node.prev

    def get_last_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next 
        
        return current_node


list = DoubleLinkedList()
list.insert_at_end(3)
list.insert_at_beginning(2)
list.insert_at_beginning(5)
list.insert_at_end(4)

# list.print_forward()
list.print_backward()