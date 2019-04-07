from utils import LinkedList


def search(ll_list, key):
    tmp = ll_list.head
    while tmp is not None:
        if tmp.data == key:
            return True
        tmp = tmp.next
    return False


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.push(4)
    linked_list.push(1)
    linked_list.append(5)
    print(search(linked_list, 43))
