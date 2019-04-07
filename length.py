from utils import LinkedList


def get_length(ll_list):
    tmp = ll_list.head
    counter = 0
    while tmp:
        tmp = tmp.next
        counter = counter + 1

    return counter


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.push(4)
    linked_list.push(1)
    linked_list.append(5)
    print(get_length(linked_list))
