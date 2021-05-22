# 5. Sort a DOUBLY linked sequential list using insertion sort algorithm.
# TASK 5
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        if self.next == None:
            return str(self.value)
        return str(self.value) + " " + self.next.__str__()


def doubleLinked(array):
    head = Node(array[0])
    head1 = head
    for a in array[1:]:
        head1.next = Node(a)
        head1 = head1.next
    head1 = head
    while True:
        if head1.next == None:
            break
        head1.next.prev = head1
        head1 = head1.next
    return head


def reverse(head):
    while True:
        if head.next == None:
            break
        head = head.next
    while True:
        print(head.value)
        if head.prev == None:
            break
        head = head.prev


def insertion_linked(head):
    head1 = head.next
    while True:
        head2 = head1
        if head1 == None:
            break
        temp = head1.value
        while True:
            if head2.prev == None:
                break
            if head2.prev.value > temp:
                head2.value = head2.prev.value
            else:
                break
            head2 = head2.prev
        head2.value = temp
        head1 = head1.next
    return head


array1 = [8, 9, 0, 6, 7, 5, 3, 4, 1, 2]
linkedlist1 = doubleLinked(array1)
print(insertion_linked(linkedlist1))
