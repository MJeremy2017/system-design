class CircularArray:
    def __init__(self):
        self.arr = []

    def insert_node(self, value):
        self.arr.append(value)

    def print_node(self, index):
        sz = len(self.arr)
        tmp_arr = self.arr + self.arr
        upper = index + sz
        while index < upper:
            print(tmp_arr[index], end=" ")
            index += 1
        print()
        print('------')

    def print_node_fast(self, index):
        sz = len(self.arr)
        upper = index + sz
        while index < upper:
            print(self.arr[index%sz], end=" ")
            index += 1
        print()
        print('##########')

    def remove_node(self, index):
        self.arr.pop(index)


class TestCircularArray:
    def test_complex(self):
        ca = CircularArray()
        ca.insert_node(3)
        ca.insert_node(12)
        ca.insert_node(43)
        ca.insert_node(4)
        ca.print_node(2)
        ca.print_node_fast(2)
        ca.print_node(1)
        ca.print_node_fast(1)


if __name__ == '__main__':
    tc = TestCircularArray()
    tc.test_complex()
