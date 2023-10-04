# singly linked list: the current node points only to the next node in sequence
# doubly linked list: the current node points both to the previous and the next node in sequence
class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val # the value of the node in the linked list
        self.next = next # the next element in sequence(default)
        # self.prev = prev # the previous element before the current node

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

# setting the next pointers for all the current elements in the linked list

one.next = two # first node points to the second node
two.next = three # second node points to the third note
head = one # head represents the start of the linked list and is how we access remaining elements

print(head.val)
print(head.next.val) # head.next.val is basically two.val
print(head.next.next.val) # head.next.next.val is basically three.val

# pointer assignment

# pointer = head # essentially saying pointer = one
# head = head.next
# head = None
# print(pointer) # pointer will always point to the original head node unless it is directly modified
# print(head) # -> prints "None"

# traversing through a linked list
def get_sum(head: ListNode) -> int:
    res = 0
    # once head reaches the third node, its value is added to res, and it then becomes null causing the while loop to end
    while head:
        res += head.val
        head = head.next
    return f'Sum of all nodes: {res}'

def print_elems(head: ListNode) -> None:
    # forward iteration in the linked list starting with the head
    while head:
        print(str(head.val) + " ")
        head = head.next

# inserting a node at a given position in a singly linked list
def insert_node(prevNode: ListNode, newNode: ListNode) -> None:
    # the new node is pointing to whatever the previous nodes next pointer was
    newNode.next = prevNode.next
    prevNode.next = newNode

insert_node(two, four) # four.next = three; two.next = four(1 -> 2 -> 4 -> 3)

# deleting a node at a given position in a singly linked list
def delete_node(prevNode: ListNode) -> None:
    # prevNode.next is the element to be deleted and here we're setting prevNodes next to what the 
    # deleted element is pointing to(3 in this case, which would remove the 4)
    prevNode.next = prevNode.next.next

delete_node(two) # deletes ListNode(4)

# inserting an element at a given index for a doubly linked list
# def insert_element(currentNode: ListNode, newNode: ListNode) -> None:
#     previousNode = currentNode.prev
#     curr = currentNode
#     newNode.next = curr
#     newNode.prev = previousNode
#     previousNode.next = newNode
#     curr.prev = newNode

# insert_element(three, four) # (1 -> 2 -> 4 -> 3)
# # previousNode = three.prev = two
# # curr = three
# # four.next = three; four.prev = two
# # two.next = four; three.prev = four

# deleting an element in a doubly linked list
# def delete_element(currentNode: ListNode) -> None:
#     previous = currentNode.prev
#     next = currentNode.next
#     previous.next = next
#     next.prev = previous

# delete_element(four) # two.next = three; three.prev = two(gets rid of four)
