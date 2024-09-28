class Node:
    def __init__(self, value = -1, l = None, n = None):
        self.last = l
        self.next = n
        self.val = value


class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.last = self.head
    

    def __len__(self) -> int:
        return self.length
    

    def is_empty(self):
        return len(self) == 0
    
    
    def is_full(self):
        return len(self) == self.capacity


    def get_front(self):
        return self.head.next
    
    
    def get_back(self):
        return self.tail.last


    def insert_front(self, new_node : Node) -> bool:
        if len(self) == self.capacity:
            return False

        temp = self.head.next
        temp.last = new_node

        new_node.next = temp
        new_node.last = self.head

        self.head.next = new_node
        self.length += 1

        return True


    def insert_back(self, new_node : Node) -> bool:
        if len(self) == self.capacity:
            return False
        
        temp = self.tail.last
        temp.next = new_node

        new_node.last = temp
        new_node.next = self.tail

        self.tail.last = new_node
        self.length += 1

        return True


    def delete_front(self):
        if len(self) == 0:
            return False
        
        self.head.next = self.head.next.next
        self.head.next.last = self.head
        
        self.length -= 1

        return True
        

    def delete_back(self):
        if len(self) == 0:
            return False
        
        self.tail.last = self.tail.last.last
        self.tail.last.next = self.tail
        
        self.length -= 1

        return True


class MyCircularDeque:

    def __init__(self, k: int):
        self.data = DoubleLinkedList(k)


    def insertFront(self, value: int) -> bool:
        return self.data.insert_front(Node(value))


    def insertLast(self, value: int) -> bool:
        return self.data.insert_back(Node(value))


    def deleteFront(self) -> bool:
        return self.data.delete_front()


    def deleteLast(self) -> bool:
        return self.data.delete_back()        


    def getFront(self) -> int:
        return self.data.get_front().val


    def getRear(self) -> int:
        return self.data.get_back().val


    def isEmpty(self) -> bool:
        return self.data.is_empty()


    def isFull(self) -> bool:
        return self.data.is_full()


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()