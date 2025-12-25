from datetime import datetime
from typing import Optional, Dict
import math
from model import Vehicle, Slot, Ticket, ParkingLotState

class ParkingLotService:  
    def __init__(self, state: ParkingLotState, hr_rate: float = 20.0):  
        self.state = state
        self.hr_rate = hr_rate
        
    def park_vehicle(self, vehicle: Vehicle):
        slot = self.state.available_slot()
        if slot is None:
            return None
        
        slot.is_occupied = True
        slot.num_plate = vehicle.num_plate

        ticket_id = self.state.current_ticket_id
        self.state.current_ticket_id += 1

        ticket = Ticket(
            ticket_id=ticket_id,
            num_plate=vehicle.num_plate,
            slot_id=slot.slot_id,
            entry_time=datetime.now()
        )

        self.state.tickets[ticket_id] = ticket
        return ticket

    def unpark_vehicle(self, ticket_id: int):
        ticket = self.state.tickets.get(ticket_id)
        if ticket is None or ticket.exit_time is not None:
            return None

        ticket.exit_time = datetime.now()
        time_tk = max((ticket.exit_time - ticket.entry_time).total_seconds() / 3600.0, 0.0)
        time_tk_ac = math.ceil(time_tk * 10) / 10
        ticket.fee = time_tk_ac * self.hr_rate

        slot = self.state.slots.get(ticket.slot_id)
        if slot:
            slot.is_occupied = False
            slot.num_plate = None
        
        return ticket

    def occupied_slots(self):
        return [s for s in self.state.slots.values() if s.is_occupied]

    def get_ticket(self, ticket_id: int):
        return self.state.tickets.get(ticket_id)
