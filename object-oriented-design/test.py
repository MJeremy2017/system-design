from collections import deque

q = deque()
q.append(3)
q.append(2)
q.appendleft(12)

print(q.popleft())