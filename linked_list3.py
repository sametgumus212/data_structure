class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, node):
        """Listenin başına ekle"""
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def add_last(self, node):
        """Listenin sonuna ekle"""
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_after(self, node, after_node):
        """Belirli bir düğümden sonra ekle"""
        if node is None or after_node is None:
            return

        if self.head is None:
            self.head = node
            self.tail = node
            return

        temp = self.head
        while temp is not None and temp.value != after_node.value:
            temp = temp.next

        if temp is None:
            print("add_after: target not found")
            return

        node.next = temp.next
        temp.next = node
        if temp == self.tail:
            self.tail = node

    def find(self, value):
        """Değere göre düğüm ara"""
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return temp
            temp = temp.next
        return None

    def remove_first(self):
        """İlk düğümü sil"""
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def remove_last(self):
        """Son düğümü sil"""
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        prev = None
        cur = self.head
        while cur != self.tail:
            prev = cur
            cur = cur.next

        prev.next = None
        self.tail = prev

    def remove_by_node(self, target):
        """Belirli düğümü sil"""
        if target is None or self.head is None:
            if self.head is None:
                print("remove_by_node: list is empty")
            return

        if self.head.value == target.value:
            print(f"removed {self.head.value}")
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        prev = None
        cur = self.head
        while cur is not None and cur.value != target.value:
            prev = cur
            cur = cur.next

        if cur is None:
            print("remove_by_node: not found")
            return

        print(f"removed {cur.value}")
        prev.next = cur.next
        if cur == self.tail:
            self.tail = prev

    def traverse(self):
        """Listedeki tüm düğümleri sırayla yazdır"""
        temp = self.head
        while temp is not None:
            print(temp.value, end="  ")
            temp = temp.next
        print()  # satır sonu


# ------------------ TEST ------------------
if __name__ == "__main__":
    lst = LinkedList()

    # 0-4 arası elemanları başa ekle
    for i in range(5):
        lst.add_first(Node(i))

    lst.traverse()
    lst.remove_first()
    print("-------------------")
    lst.traverse()
    lst.remove_last()
    print("-------------------")
    lst.traverse()
    print("-------------------")

    nb = Node(4)
    ns = Node(0)
    na = Node(1)
    nn = Node(3)

    lst.add_first(nb)
    lst.traverse()

    print("-------------------")
    lst.add_last(ns)
    lst.traverse()

    print("-------------------")
    # lst.add_after(na, nn)
    print("-------------------")
    lst.traverse()

    lst.remove_by_node(na)
    lst.traverse()
