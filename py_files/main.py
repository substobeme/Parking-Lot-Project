from model import ParkingLotState
from services import ParkingLotService
from gui import gui

def run_app():
    state = ParkingLotState(total_slots=20)
    service = ParkingLotService(state=state, hr_rate=20.0)
    gui(service)

if __name__ == "__main__":
    run_app()
