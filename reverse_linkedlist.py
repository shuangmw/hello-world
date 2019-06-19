class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_recursion(head):
    if head == None or head.next == None:
        return head

    head_new = reverse_recursion(head.next)
    head.next.next = head
    head.next = None
    return head_new


def reverse_loop(head):
    if head == None or head.next == None:
        return head

    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def create_ll(arr):
    head = ListNode(0)
    tmp = head
    for i in arr:
        head.next = ListNode(i)
        head = head.next
    return tmp.next


def print_ll(head):
    while head:
        print head.val
        head = head.next


head = create_ll(range(5))
head = reverse_loop(head)
print_ll(head)
