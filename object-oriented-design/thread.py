from collections import deque
import threading
import time


class Record:
    def __init__(self, val, ts):
        self.val = val
        self.ts = ts


class Pipe:
    def __init__(self):
        self.q = deque()
        self.start_time = -1
        self.s = 0
        self.size = 0
        self.thd = threading.Thread(target=self._remove_expired)
        self.thd.start()
        self.thd.join()

    def _remove_expired(self):
        while 1:
            ts = time.time()
            if self.start_time != -1 and ts - self.start_time >= 5:
                self.s -= self.q[0].val
                self.q.popleft()
                self.size -= 1
            print("here")
            time.sleep(10)

    def record(self, val, ts):
        print('record element', val)
        # self._remove_expired(ts)
        self.start_time = self.q[0].ts if len(self.q) else ts
        self.q.append(Record(val, ts))
        self.s += val
        self.size += 1

    def get_mean(self, ts):
        # self._remove_expired(ts)
        self.start_time = self.q[0].ts if len(self.q) else ts
        return self.s / self.size


pe = Pipe()

pe.record(11, 1)
pe.record(1, 2)
pe.record(5, 3)
pe.record(3, 4)
t = pe.get_mean(5)
print(t, pe.start_time)
t = pe.get_mean(6)
print(t, pe.start_time)

