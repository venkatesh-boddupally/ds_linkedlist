class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print('Previous node must be in linked list')
            return None
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return None

        prev.next = temp.next
        temp = None

    def delete_at_p(self, position):

        if self.head is None:
            return

        tmp = self.head

        if position == 0:
            self.head = tmp.next
            tmp = None
            return

        for i in range(position - 1):
            tmp = tmp.next
            if tmp is None:
                break

        if tmp is None:
            return
        if tmp.next is None:
            return

        next = tmp.next.next

        tmp.next = None

        tmp.next = next


if __name__ == '__main__':
    l_list = LinkedList()

    l_list.append(3)
    l_list.push(1)
    l_list.insert_after(l_list.head, 2)
    l_list.print_list()
    print('____________________________')
    l_list.delete(1)
    l_list.print_list()
    print('------------------------')
    l_list.delete_at_p(0)
    l_list.print_list()
