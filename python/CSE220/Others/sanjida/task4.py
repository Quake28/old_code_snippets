# 4. Sort a singly linked sequential list using selection sort algorithm.
# TASK 4
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.value)
        return str(self.value) + " " + self.next.__str__()


def singlyLinked(array):
    head = Node(array[0])
    head1 = head
    for a in array[1:]:
        head1.next = Node(a)
        head1 = head1.next
    head1 = head
    return head


def selection_linked(head):
    head1 = head
    while True:
        head2 = head1.next
        min = head1
        if head1.next == None:
            break
        while True:
            if min.value > head2.value:
                min = head2
            if head2.next == None:
                break
            head2 = head2.next
        temp = min.value
        min.value = head1.value
        head1.value = temp
        head1 = head1.next
    return head


array1 = [8, 9, 0, 6, 7, 5, 3, 4, 1, 2]
linkedlist1 = singlyLinked(array1)
print(selection_linked(linkedlist1))
