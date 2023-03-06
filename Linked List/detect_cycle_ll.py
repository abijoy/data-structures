from singly_ll import LinkedList, Node

# Time --> O(n)  Space --> O(n)
def detect_cycle_ll(head: Node) -> bool:
    nodes = set()
    curr_node = head
    while curr_node:
        print(curr_node.data)
        if nodes.__contains__(curr_node):
            return True
        nodes.add(curr_node)
        curr_node = curr_node.next
    return False

# Time --> O(n)  Space --> O(1)
def detect_cycle_ll_runner_walker(head: Node) -> bool:
    if head == None:
        return False
    walker = head
    runner = head 

    while(runner.next and runner.next.next):
        walker = walker.next
        runner = runner.next.next
        if (walker == runner):
            return True
    return False



llist = LinkedList()
llist.append(9)
llist.append(8)
llist.append(7)
llist.append(6)

# building a cycle
llist.head.next.next.next.next = llist.head


# llist.printList()

print(detect_cycle_ll(llist.head))
print(detect_cycle_ll_runner_walker(llist.head))

