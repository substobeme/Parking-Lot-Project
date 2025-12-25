from dataclasses import dataclass
from datetime import datetime
from typing import Optional,Dict

@dataclass
class Vehicle:
    num_plate: str
    vehicle_type: str

@dataclass
class Ticket:
    ticket_id:int
    num_plate:str
    slot_id: int
    entry_time:datetime
    exit_time: Optional[datetime]=None
    fee: float=0.0

@dataclass
class Slot:
    slot_id:int
    is_occupied: bool=False
    num_plate: Optional[str]=None

class ParkingLotState:
    def __init__(self, total_slots: int):
        self.slots: Dict[int, Slot] = {}
        self.tickets: Dict[int, Ticket] = {}
        self.current_ticket_id: int = 1556729

        for slot_id in range(1, total_slots + 1):
            self.slots[slot_id] = Slot(slot_id=slot_id)

    def available_slot(self):
        for slot in self.slots.values():
            if not slot.is_occupied:
                return slot
        return None

    def available_slots_count(self):
        return len([s for s in self.slots.values() if not s.is_occupied])


