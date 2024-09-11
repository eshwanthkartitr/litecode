from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.ca=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.ca:
            self.ca.move_to_end(key)
            return self.ca[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ca:
            self.ca[key]=value
            self.ca.move_to_end(key)
        else:
            self.ca[key]=value
            self.ca.move_to_end(key)
            if len(self.ca)>self.cap:
                self.ca.popitem(last=False)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)