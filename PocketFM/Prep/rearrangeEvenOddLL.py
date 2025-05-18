"""
Rearrange a linked list with numbers such that odd numbers come first, followed by
even number order being maintained.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rearrange_odd_even(head):
    if not head or not head.next:
        return head

    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_tail, even_tail = odd_dummy, even_dummy

    current = head
    while current:
        next_node = current.next
        current.next = None  # Detach node

        if current.val % 2 != 0:
            odd_tail.next = current
            odd_tail = odd_tail.next
        else:
            even_tail.next = current
            even_tail = even_tail.next
        current = next_node

    # Connect odd list to even list
    odd_tail.next = even_dummy.next
    return odd_dummy.next if odd_dummy.next else even_dummy.next

# Helper functions
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Test
head = create_linked_list([0, 3])
new_head = rearrange_odd_even(head)
print_linked_list(new_head)
