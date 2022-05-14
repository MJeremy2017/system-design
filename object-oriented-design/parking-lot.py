import random


class Spot:
    def __init__(self, id: str, tp: int, empty: bool = True):
        self.id: str = id
        self.tp: int = tp
        self.empty: bool = empty

    def __str__(self):
        return f"lot_id {self.id} | car_type {self.tp} | empty {self.empty}"


class ParkingLot:
    def __init__(self, n_floor, n_row, n_col):
        self.occupied_count = None
        self.empty_count = None
        self.empty_lots = []
        self.pk_lot = {}
        self.n_floor = n_floor
        self.n_row = n_row
        self.n_col = n_col
        self.initialise()

    def initialise(self):
        for i in range(self.n_floor):
            f = []
            for j in range(self.n_row):
                row = []
                for k in range(self.n_col):
                    spot = self._get_random_spot(i, j, k)
                    row.append(spot)
                    self.empty_lots.append(spot)
                f.append(row)
            self.pk_lot[i] = f
        self.empty_count = self.n_floor * self.n_row * self.n_col
        self.occupied_count = 0

    def park(self, car_type: int) -> Spot:
        lot: Spot = self.empty_lots.pop(0)
        id: str = lot.id
        floor, row, col = map(int, list(id))
        lot.empty = False
        self.pk_lot[floor][row][col] = lot
        self.empty_count -= 1
        self.occupied_count += 1
        return lot

    def leave(self, lot: Spot):
        id: str = lot.id
        floor, row, col = map(int, id.split(""))
        lot.empty = True
        self.pk_lot[floor][row][col] = lot
        self.empty_count += 1
        self.occupied_count -= 1

    def get_empty_count(self):
        return self.empty_count

    def get_occupied_count(self):
        return self.occupied_count

    def _get_random_spot(self, floor, row, col):
        id = self._get_encode_id(floor, row, col)
        return Spot(id, random.randint(0, 3), True)

    def _get_encode_id(self, floor, row, col):
        return str(floor)+str(row)+str(col)


class TestParkingLot:
    def __init__(self):
        self.parking_log = ParkingLot(1, 2, 10)

    def test_get_count(self):
        self.parking_log.park(1)
        got_oc_cnt = self.parking_log.get_occupied_count()
        want_oc_cnt = 1
        assert got_oc_cnt == want_oc_cnt
        got_empty_cnt = self.parking_log.get_empty_count()
        want_empty_cnt = 19
        assert got_empty_cnt == want_empty_cnt
        print("test_get_count passed")


if __name__ == '__main__':
    tpk = TestParkingLot()
    tpk.test_get_count()
