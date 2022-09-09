class RandomizedSet:
    
    def __init__(self):
        self.items = []

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# print(obj.insert(1))
# print(obj.remove(2))
# print(obj.insert(2))
# print(obj.getRandom())