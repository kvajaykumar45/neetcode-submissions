class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        bucket = self.buckets[self._hash(key)]
        for x in bucket:
            if x == key:
                return
        bucket.append(key)

    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for i in range(len(bucket)):
            if bucket[i] == key:
                del bucket[i]
                return

    def contains(self, key):
        bucket = self.buckets[self._hash(key)]
        for x in bucket:
            if x == key:
                return True
        return False       


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)