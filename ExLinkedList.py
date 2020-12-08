

class LinkedList():

    def __init__(self):
        self.head = None

    def insert_middle_node(self, pre, data:str):
        new_node = ListNode(data)
        new_node.link = pre.link
        pre.link = new_node

    def insert_last_node(self, data:str):
        new_node = ListNode(data)
        if(self.head is None):
            self.head = new_node
        else:
            tmp_node = self.head
            while tmp_node.link != None:
                tmp_node = tmp_node.link
            tmp_node.link = new_node

    def delete_last_node(self):
        prev_node = None
        temp = None
        if self.head is None:
            return
        if self.head.link is None:
            self.head = None
        else:
            prev_node = self.head
            temp = self.head.link
            while temp.link != None:
                prev_node = temp
                temp = temp.link
            prev_node.link = None;

    def search_node(self, data:str):
        rx_node = self.head
        while rx_node != None:
            if data == rx_node.get_data():
                return rx_node
            else:
                rx_node = rx_node.link
        return rx_node

    def reverse_list(self):
        next = self.head
        current = None
        pre = None
        while next != None:
            pre = current
            current = next
            next = next.link
            current.link = pre
        self.head = current

    def print_list(self):
        tmp = self.head
        print("list = (")
        while (tmp != None):
            print(tmp.get_data())
            tmp = tmp.link
            if tmp != None:
                print(',')
        print(")")


class ListNode():

    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def get_data(self):
        return self.data


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_last_node("JAN")
    linked_list.insert_last_node("FEB")
    linked_list.insert_last_node("MAR")
    linked_list.print_list()

    pre = linked_list.search_node("FEB")
    print(pre)

