# Contest logic and modes.
import random
from simulation.conditions import simulate_band_conditions

class ContestManager:
    def __init__(self, duration=60, mode="Pile-Up"):
        self.duration = duration
        self.mode = mode
        self.log = []
        self.active = False

    def start_contest(self):
        self.active = True
        for minute in range(self.duration):
            band_conditions = simulate_band_conditions()
            print(f"Minute {minute}: Band Conditions: {band_conditions}")
            self.log.append(band_conditions)
        self.active = False

    def save_log(self, file_path):
        with open(file_path, "w") as file:
            for entry in self.log:
                file.write(f"{entry}\n")