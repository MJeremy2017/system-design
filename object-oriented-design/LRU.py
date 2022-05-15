class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.mp = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self._remove(node)
        self._add(node)
        return node.value

    def set(self, key, value):
        node_new = Node(key, value)
        if key in self.mp:
            node = self.mp[key]
            self._remove(node)
            self._add(node_new)
            return
        if len(self.mp) == self.capacity:
            tmp = self.tail.prev
            self._remove(tmp)
        self._add(node_new)

    def _remove(self, node):
        self.mp.pop(node.key)
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def _add(self, node):
        self.mp[node.key] = node
        tmp = self.head.nxt
        self.head.nxt = node
        node.prev = self.head
        node.nxt = tmp
        tmp.prev = node


class TestLRU:
    def __init__(self):
        self.lru = LRU(2)

    def test(self):
        self.lru.set(3, 3)
        self.lru.set(2, 2)
        got = self.lru.get(2)
        want = 2
        self.assert_equal(got, want)

        self.lru.set(1, 1)
        got = self.lru.get(3)
        want = -1
        self.assert_equal(got, want)

    def assert_equal(self, got, want):
        if got != want:
            raise Exception(f"got {got} want {want}")


if __name__ == '__main__':
    tlru = TestLRU()
    tlru.test()
