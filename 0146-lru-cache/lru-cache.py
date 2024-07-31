class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.prev = None
            self.next = None
            self.key = key
            self.val = val

    def add_node(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
    
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __init__(self, capacity: int):
        self.vals = dict()
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        answer = -1
        if key in self.vals:
            answer = self.vals[key].val
            temp = self.vals[key]
            self.delete_node(temp)
            self.add_node(temp)
        
        return answer

    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            self.vals[key].val = value
            self.get(key)
            return

        if len(self.vals) == self.capacity:
            old_node = self.tail.prev
            del self.vals[old_node.key]
            self.delete_node(old_node)

        new_node = self.Node(key, value)
        self.add_node(new_node)
        self.vals[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)