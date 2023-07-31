class ListNode():
    def __init__(self, val):
        self.val = val # the value of the node in the linked list
        self.next = None # the next element in sequence(default)

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two # first node points to the second node
two.next = three # second node points to the third note
head = one # head represents the start of the linked list and is how we access remaining elements

print(head.val)
print(head.next.val) # head.next.val is basically two.val
print(head.next.next.val) # head.next.next.val is basically three.val

# pointer assignment

# pointer = head
# head = head.next
# head = None
# print(pointer) # pointer will always point to the original head node unless it is directly modified
# print(head) -> prints "None"

# traversing through a linked list
def get_sum(head: ListNode) -> int:
    res = 0
    # once head reaches the third node, its value is added to res, and it then becomes null causing the while loop to end
    while head:
        res += head.val
        head = head.next
    return f'Sum of all nodes: {res}'

print(get_sum(head))

# inserting a node at a given position
def insert_node(prevNode: ListNode, newNode: ListNode) -> None:
    # the new node is pointing to whatever the previous nodes next pointer was
    newNode.next = prevNode.next
    prevNode.next = newNode

insert_node(two, ListNode(4))

while head:
    print(head.val) # prints 1, 2, 4, 3
    head = head.next