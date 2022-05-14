from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from queue import PriorityQueue
import time


class CarType(Enum):
    MOTOR_BIKE = 1
    CAR = 2
    BUS = 3


class CarSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Ticket:
    def __init__(self, ticket_id: str, entered_at: int, left_at: int, license_plate: str, level: int, spot_id: str):
        self.ticket_id = ticket_id
        self.entered_at = entered_at
        self.left_at = left_at
        self.license_plate = license_plate
        self.level = level
        self.spot_id = spot_id


class TicketEngine:
    def __init__(self):
        self.id = 0

    def create_entry_ticket(self, vehicle: Vehicle, level: Level, spot: ParkingSpot, time: int):
        return Ticket(self.gen_id(), time, -1, vehicle.license_plate, level.level_id, spot.spot_id)

    def create_leave_ticket(self, entry_ticket: Ticket, time: int):
        entry_ticket.left_at = time
        return entry_ticket

    def gen_id(self) -> str:
        ticket_id = self.id
        self.id += 1
        return str(ticket_id)


class Vehicle:
    def __init__(self, license_plate: str, car_type: CarType, size: CarSize):
        self.license_plate = license_plate
        self.car_type = car_type
        self.car_size = size

    def __str__(self):
        return f"license: {self.license_plate} car_type: {self.car_type.name}"


class MotorBike(Vehicle):
    def __init__(self, license_plate: str, car_type: CarType, size: CarSize):
        super().__init__(license_plate, car_type, size)


class Car(Vehicle):
    def __init__(self, license_plate: str, car_type: CarType, size: CarSize):
        super().__init__(license_plate, car_type, size)


class Bus(Vehicle):
    def __init__(self, license_plate: str, car_type: CarType, size: CarSize):
        super().__init__(license_plate, car_type, size)


class Spot(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def park_vehicle(self, vehicle):
        pass


class NullSpot(Spot):
    def __init__(self, size=0):
        super().__init__(size)

    def is_empty(self) -> bool:
        return False

    def park_vehicle(self, vehicle):
        raise Exception("You can not part at null spot")


class ParkingSpot(Spot):
    def __init__(self, spot_id: str, size: CarSize, level: int, vehicle: Vehicle = None):
        super().__init__(size)
        self.spot_id = spot_id
        self.vehicle = vehicle
        self.level = level

    def park_vehicle(self, vehicle: Vehicle):
        if self.vehicle is not None:
            raise ValueError(f"Spot is parked by {vehicle}")
        if self._valid_size(vehicle):
            self.vehicle = vehicle
        else:
            raise ValueError(f"{vehicle} can not parked in the spot of size {self.size}")

    def is_empty(self) -> bool:
        return self.vehicle is None

    def _valid_size(self, vehicle: Vehicle) -> bool:
        if self.size.value >= vehicle.car_type.value:
            return True
        return False

    def remove_parking(self):
        self.vehicle = None

    def __lt__(self, other: Spot):
        return self.size < other.size


class Level:
    def __init__(self, level: int):
        self.level_id = level
        self.spots: List[ParkingSpot] = []
        self.empty_spots: PriorityQueue[ParkingSpot] = PriorityQueue()
        self.empty_spot_count = 0
        self.occupied_spot_count = 0

    def add_spot(self, spot: ParkingSpot):
        if spot.is_empty():
            self.empty_spots.put(spot)
        self.spots.append(spot)
        self._update_count(spot)

    def get_smallest_empty_spot(self, vehicle: Vehicle) -> Spot:
        vehicle_size = vehicle.car_type
        while not self.empty_spots.empty():
            size, spot = self.empty_spots.get()
            if spot.size >= vehicle_size and spot.is_empty():
                return spot
            self.empty_spots.put(spot)
        return NullSpot()

    def _update_count(self, spot: ParkingSpot):
        if spot.is_empty():
            self.empty_spot_count += 1
            self.occupied_spot_count -= 1
        else:
            self.occupied_spot_count += 1
            self.empty_spot_count -= 1

    def park(self, vehicle: Vehicle):
        spot: Spot = self.get_smallest_empty_spot(vehicle)
        if isinstance(spot, NullSpot):
            return spot
        self._update_count(spot)
        return spot

    def unpark(self, spot: ParkingSpot):
        spot.vehicle = None
        self.empty_spots.put(spot)
        self._update_count(spot)


class ParkingLot:
    def __init__(self, ticket_engine: TicketEngine):
        self.levels: List[Level] = []
        self.mapping_position = {}
        self.vehicle_ticket = {}
        self.ticket_engine = ticket_engine

    def park_vehicle(self, vehicle: Vehicle):
        spot: Spot = NullSpot()
        for level in self.levels:
            spot: Spot = level.park(vehicle)
            if isinstance(spot, ParkingSpot):
                self.mapping_position[vehicle] = (level, spot)
                ticket = self.ticket_engine.create_entry_ticket(vehicle, level, spot, int(time.time()))
                self.vehicle_ticket[vehicle] = ticket
                break
        if isinstance(spot, NullSpot):
            print("No vacant spot at the moment!")
            return

    def unpark(self, vehicle: Vehicle):
        if vehicle not in self.mapping_position:
            return
        level, spot = self.mapping_position[vehicle]
        level.unpark(spot)
        ticket = self.ticket_engine.create_leave_ticket(self.vehicle_ticket[vehicle], int(time.time()))
        return ticket

    def add_level(self, level: Level):
        self.levels.append(level)

    def _get_parking_spot(self, vehicle: Vehicle) -> Spot:
        for level in self.levels:
            spot: Spot = level.get_smallest_empty_spot(vehicle)
            if spot is not None:
                return spot
        return NullSpot()


if __name__ == '__main__':
    ct = CarType.BUS
    print(ct.name)
