
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(to_list(self))

def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)

def to_list(head):
    values = []
    i = head
    while i:
        values.append(i.val)
        i = i.next
    return values

def from_list(l):
    if not l:
        return None
    
    head = ListNode(l[0])  # Create the head node from the first element
    current = head

    for i in range(1, len(l)):
        new_node = ListNode(l[i])
        current.next = new_node
        current = new_node
    
    return head

