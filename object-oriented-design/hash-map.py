KEY_ERROR_MESSAGE = "key '{}' does not exist!"


class HashMap:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(size)]

    def set(self, key: int, value: object):
        hashed_key = self._get_hash_key(key)
        if len(self.arr[hashed_key]) == 0:
            self.arr[hashed_key].append([key, value])
            return
        for i, (k, _) in enumerate(self.arr[hashed_key]):
            if k == key:
                self.arr[hashed_key][i] = [key, value]
                return
        self.arr[hashed_key].append([key, value])

    def get(self, key) -> object:
        hashed_key = self._get_hash_key(key)
        if len(self.arr[hashed_key]) == 0:
            raise KeyError(KEY_ERROR_MESSAGE.format(key))
        for k, v in self.arr[hashed_key]:
            if k == key:
                return v
        raise KeyError(KEY_ERROR_MESSAGE.format(key))

    def remove(self, key):
        hashed_key = self._get_hash_key(key)
        if len(self.arr[hashed_key]) == 0:
            return
        for i, (k, v) in enumerate(self.arr[hashed_key]):
            if k == key:
                del self.arr[i]

    def _get_hash_key(self, key):
        return key % self.size


class TestCase:
    def __init__(self, inp, wanted):
        self.inp = inp
        self.wanted = wanted


class TestHashMap:
    def __init__(self):
        self.map = HashMap(100)

    def test_set_get(self):
        test_cases = [
            TestCase((3, 'abc'), 'abc')
        ]

        for tc in test_cases:
            key, value = tc.inp[0], tc.inp[1]
            wanted = tc.wanted
            self.map.set(key, value)
            got = self.map.get(key)
            self._assert_equal(got, wanted)

    def test_remove(self):
        test_cases = [
            TestCase((3, 'abc'), "key '3' does not exist!")
        ]
        for tc in test_cases:
            key, value = tc.inp[0], tc.inp[1]
            self.map.set(key, value)
            self.map.remove(key)
            try:
                self.map.get(key)
            except Exception as e:
                print(e)

    def _assert_equal(self, got, wanted):
        if got != wanted:
            msg = f"assertion failed got '{got}' want '{wanted}'"
            raise Exception(msg)


if __name__ == '__main__':
    test_obj = TestHashMap()
    test_obj.test_set_get()
    test_obj.test_remove()
