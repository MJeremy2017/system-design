from queue import PriorityQueue


class Node:
    def __init__(self, node_idx, current_rate):
        self.node_idx = node_idx
        self.current_rate = current_rate

    def __lt__(self, other):
        return self.current_rate > other.current_rate


class CurrencyExchange:

    def find_best_conversion_path(self, from_c, to_c, graph: dict):
        """
        :param to_c:
        :param from_c:
        :param graph: {coin_index: [(coin_index, rate), ...]}
        :return:
        """
        n = len(graph)
        weights = [-float('inf')] * n
        parent = [i for i in range(n)]
        weights[from_c] = 1
        q = PriorityQueue()
        q.put(Node(from_c, 1))

        while not q.empty():
            node: Node = q.get()
            coin, rate = node.node_idx, node.current_rate
            for ngb_coin, weight in graph[coin]:
                if rate * weight > weights[ngb_coin]:
                    weights[ngb_coin] = rate * weight
                    parent[ngb_coin] = coin
                    q.put(Node(ngb_coin, rate * weight))

        full_path = self._get_path(parent, to_c)
        return weights[to_c], full_path

    def find_best_conversion_rate_bf(self, from_c, to_c, graph: dict):
        # Bellman Ford
        n = len(graph)
        weights = [-float('inf')] * n
        weights[from_c] = 1
        parents = [i for i in range(n)]

        for node in range(n - 1):
            curr_w = weights[node]
            for ngb, w in graph[node]:
                if curr_w * w > weights[ngb]:
                    weights[ngb] = curr_w * w
                    parents[ngb] = node
        paths = []
        s = to_c
        while parents[s] != s:
            paths.append(s)
            s = parents[s]
        paths.append(from_c)
        return weights[to_c], paths[::-1]

    def _get_path(self, parent, to_c):
        p = []

        def _dfs(node):
            p.append(node)
            if parent[node] == node:
                return
            _dfs(parent[node])

        _dfs(to_c)
        return p[::-1]


class TestCurrencyExchange:
    g = {0: [(1, 10), (2, 20), (3, 2.5)], 1: [(0, 0.1), (3, 0.5)], 2: [(0, 1 / 20.0), (3, 0.1)], 3: [(1, 1 / 2.5)]}

    def test_conversion_path(self):
        ex = CurrencyExchange()
        w = ex.find_best_conversion_path(0, 3, g)
        print(w)

    def test_conversion_path_bf(self):
        ex = CurrencyExchange()
        w = ex.find_best_conversion_rate_bf(0, 3, g)
        print(w)


if __name__ == '__main__':
    tex = TestCurrencyExchange()
    tex.test_conversion_path()
    print("-----------")
    tex.test_conversion_path_bf()
