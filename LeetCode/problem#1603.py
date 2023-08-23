class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.hashTable = {1: big, 2: medium, 3: small}
        # self.hashTable = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        result = self.hashTable[carType]
        if result:
            self.hashTable[carType-1] -= 1
            return True
        return False

