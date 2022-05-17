"""
User search for someone and return the shortest path
"""

import heapq as hq


class Search:
    def __init__(self, graph):
        # graph of user connections
        self.graph: dict = graph
        self.users = list(graph.keys())
        self.n_user = len(self.users)

        self.user_id = {}
        self.id_user = {}
        for i, u in enumerate(self.users):
            self.user_id[u] = i
            self.id_user[i] = u

    def search(self, source_user, dest_user):
        weights = [float('inf')] * self.n_user
        parents = [i for i in range(dest_user)]
        q = [(0, self.user_id[source_user])]
        hq.heapify(q)

        while len(q):
            cost, u_id = hq.heappop(q)
            if u_id == self.users[dest_user]:
                break
            for ngb in self.graph[self.id_user[u_id]]:
                if 1 + cost < weights[self.user_id[ngb]]:
                    hq.heappush(q, (1 + cost, self.user_id[ngb]))
                    parents[ngb] = cost

        path = self._get_path(parents, source_user, dest_user)
        return path

    def _get_path(self, parents, source_user, dest_user):
        path = []
        while parents[dest_user] != source_user:
            path.append(dest_user)
            dest_user = parents[dest_user]
        path.append(source_user)
        return path[::-1]
