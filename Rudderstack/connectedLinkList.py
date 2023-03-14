# code to find if a linklist is connected or not...

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def connectedList(head1, head2):
    # if head1==None or head2==None:
    #     return
    
    # end1 = None
    # end2 = None
    while head1.next:
        head1 = head1.next

    # end1 = head1
    
    while head2.next:
        head2 = head2.next

    # end2 = head2

    if head1.data == head2.data:
        return True
    return False



if __name__ == "__main__":
    
    head1 = Node(90)
    head1.next = Node(80)
    head1.next.next = Node(87)
    head1.next.next.next = Node(75)

    head2 = Node(91)
    head2.next = Node(89)
    head2.next.next = Node(75)

    res = connectedList(head1, head2)
    print(res)
    