# --------------
# 148. Sort List
# --------------

# Problem: https://leetcode.com/problems/sort-list
# 
# Given the head of a linked list, return the list after sorting it in ascending order.
# 
# Example 1:
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# Example 2:
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# Example 3:
# 
# Input: head = []
# Output: []
# 
#  
# Constraints:
# 
# 	The number of nodes in the list is in the range [0, 5 * 104].
# 	-105 <= Node.val <= 105
#  
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)

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

# Solution: https://youtu.be/TGveA1oFhrc
# Credit: Navdeep Singh founder of NeetCode
def sort_list(head):
    if not head or not head.next:
        return head

    mid = get_mid(head)
    left, right = sort_list(head), sort_list(mid)

    return merge_two_sorted(left, right)

def merge_two_sorted(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    sentinel = ListNode()
    prev = sentinel
    while list1 and list2:
        if list1.val < list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    if list1:
        prev.next = list1
    else:
        prev.next = list2

    return sentinel.next

def get_mid(head):
    mid_prev = None
    while head and head.next:
        mid_prev = mid_prev.next if mid_prev else head
        head = head.next.next

    mid = mid_prev.next
    mid_prev.next = None

    return mid

def main():
    l = from_list([4,2,1,3])
    result = sort_list(l)
    print(to_list(result)) # [1,2,3,4]

    l = from_list([-1,5,3,4,0])
    result = sort_list(l)
    print(to_list(result)) # [-1,0,3,4,5]

if __name__ == "__main__":
    main()
