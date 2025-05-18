"""
#   Rearrange a linked list

Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together 
and all even position nodes are together. (Considering 1-based indexing.)

Note: You should place all odd-positioned nodes first and then the even-positioned ones. Also, the relative
order of odd-positioned nodes and even-positioned nodes should be maintained. 

Examples:

Input: LinkedList: 1->2->3->4
Output: 1->3->2->4 
Explanation: Odd elements are 1, 3 and even elements are 2, 4. Hence, resultant linked list is 1->3->2->4
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        
def rearrangeEvenOdd(head):
    #code here
    ptr=head
    cur=head.next
    k=cur
    while(ptr.next!=None and cur.next!=None):
        ptr.next=cur.next
        ptr=cur.next
        cur.next=ptr.next
        cur=ptr.next
    ptr.next=k
    return head
    
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    print("Linked list:")
    print_linked_list(head)
    
    k = 3 
    
    rearrangeEvenOdd(head)
    
    print("Linked list after re-arrangement: ")
    print_linked_list(head)
    
  
