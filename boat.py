class Boat():
    def __init__(self, howItMoves, type):
        self.howItMoves = howItMoves
        self.type = type
    def move(self, speed):
        return f"The {self.type} moves with a {self.howItMoves} at {speed} meters per second."

class Kayak(Boat):
    def __init__(self):
        super().__init__("paddle", "kayak")

blueKayak = Kayak()
print(blueKayak.howItMoves)
print(blueKayak.move(6))