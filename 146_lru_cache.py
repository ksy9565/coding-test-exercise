from collections import OrderedDict

### OrderdDict에 모든 기능이 있음...
### Java는 LinkedHashMap(accessOrder=true + removeEldestEntry 오버라이드)
### C++은 list + unordered_map<int, list<...>::iterator>

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

### 직접 구현
# class Node:
#     def __init__(self, key=0, val=0):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None
#         # 이중 연결 리스트


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map = {} # key-value 자료구조. 파이썬에서는 딕셔너리
#         self.first = Node()
#         self.last = Node()
#         self.first.prev = self.last
#         self.last.next = self.first

#     def remove(self, node: Node) -> None:
#         node.prev.next = node.next
#         node.next.prev = node.prev
    
#     # ---시간순--->
#     # First-Last
#     # First-1-Last
#     # First-1-2-Last
#     # First-1-2-3-Last 형태로 입력됨
#     def add_to_last(self, node: Node) -> None:
#         node.next = self.last.next
#         node.prev = self.last
#         self.last.next.prev = node
#         self.last.next = node

#     def get(self, key: int) -> int:
#         if key not in self.map:
#             return -1
#         node = self.map[key]
#         self.remove(node)
#         self.add_to_last(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.map:
#             node = self.map[key]
#             node.val = value
#             self.remove(node)
#             self.add_to_last(node)
#             return
        
#         if len(self.map) == self.capacity:
#             lru_node = self.first.prev
#             self.remove(lru_node)
#             del self.map[lru_node.key]
        
#         node = Node(key, value)
#         self.map[key] = node
#         self.add_to_last(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)