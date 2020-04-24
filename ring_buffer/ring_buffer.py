from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.length = 0

    def append(self, item):

        if self.length < self.capacity:
            if self.length == 0:
                self.storage.add_to_head(item)
                self.length += 1
            else:
                self.storage.add_to_tail(item)
                self.current = self.storage.tail
                self.length += 1
        elif self.length == self.capacity:
            if self.current.next == None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item
        # cur = self.storage.head
        # for steps in range(self.capacity):
        #     if steps == self.ptr:
        #         cur.value = item
        #         if self.ptr == self.capacity:
        #             self.ptr = 0
        #         else:
        #             self.ptr += 1
        #     cur = cur.next

        # if self.ptr == self.capacity:
        #     self.ptr = 0
        # else:
        #     self.ptr += 1
        #
        # i = 0
        # cur = self.storage.head
        # if i == self.ptr:
        #     cur.value = item
        # else:
        #     while i < self.ptr:
        #         i += 1
        #         cur = cur.next
        #         if i == self.ptr:
        #             cur.value = item



        #
        # while self.oldest == None:
        #
        #     if self.length == 0:
        #         self.storage.add_to_head(item)
        #         self.length += 1
        #     elif self.length < self.capacity:
        #         self.storage.add_to_tail(item)
        #         self.length +=1
        #     elif self.length == self.capacity:
        #         self.storage.add_to_tail(item)
        #         self.storage.remove_from_head()
        #         self.oldest = self.storage.head.next
        #


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur = self.storage.head
        while cur:
            if cur.value:
                list_buffer_contents.append(cur.value)
            cur = cur.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
