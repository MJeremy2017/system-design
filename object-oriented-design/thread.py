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
        self.start_background_task()

    def _remove_expired(self):
        while 1:
            time.sleep(1)
            print("clearing ...")
            if len(self.q) == 0:
                continue
            ts = time.time()
            if self.start_time != -1 and ts - self.start_time >= 5:
                self.s -= self.q[0].val
                self.q.popleft()
                self.size -= 1

    def record(self, val, ts):
        self.start_time = self.q[0].ts if len(self.q) else ts
        self.q.append(Record(val, ts))
        self.s += val
        self.size += 1

    def get_mean(self, ts):
        self.start_time = self.q[0].ts if len(self.q) else ts
        return self.s / self.size

    def start_background_task(self):
        thd = threading.Thread(target=self._remove_expired)
        thd.start()


pe = Pipe()

pe.record(11, 1)
pe.record(1, 2)
pe.record(5, 3)
pe.record(3, 4)
t = pe.get_mean(5)
print(t, pe.start_time)
t = pe.get_mean(6)
print(t, pe.start_time)

