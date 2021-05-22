# 3. Sort a singly linked sequential list using bubble sort algorithm.
# TASK 3
class Node:
    def __init__(self, value=None, next=None):
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
    return head


def bubble_linked(head):
    head1 = head
    while True:
        head2 = head
        if head1.next == None:
            break
        while True:
            if head2.next == None:
                break
            if head2.value > head2.next.value:
                temp = head2.next.value
                head2.next.value = head2.value
                head2.value = temp
            head2 = head2.next
        head1 = head1.next
    return head


array1 = [8, 9, 0, 6, 7, 5, 3, 4, 1, 2]
# reverse(linkedlist1)


linkedlist1 = singlyLinked(array1)
print(bubble_linked(linkedlist1))
