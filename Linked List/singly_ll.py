# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head == new_node
            return
        tmp_node = self.head
        self.head = new_node
        self.head.next = tmp_node

    def delete_node(self, key):
        curr_node = self.head
        # key is at the begining 
        if curr_node and curr_node.data == key:
            self.head = self.head.next
            curr_node = None #free up space
            return
        
        # key is not at the begining
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        # if current node went through the last node without finding the key
        # then the key is not in the list, therefore return.
        if curr_node == None:
            return

        prev_node.next = curr_node.next
        curr_node = None 

    def delete_node_pos(self, pos):
        curr_node = self.head
        # first position
        if pos == 0:
            self.head = self.head.next
            return
        # position at any point
        prev_node = None
        i = 0
        for i in range(pos):
            prev_node = curr_node
            curr_node = curr_node.next
            # print(f'prev -> {prev_node.data} curr -> {curr_node.data}')

        prev_node.next = curr_node.next
        curr_node = None

    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(9)
    llist.append(8)
    llist.append(7)

    llist.prepend(1)
    llist.prepend(2)
    llist.append(6)

    llist.printList()
    llist.delete_node_pos(5)
    llist.printList()
