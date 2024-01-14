class Robot1:
    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, distance):
        for i in range(1, distance + 1):
            self.batteryCharge -= 0.5
            print(f"[{i}]", end=" ")
            if self.batteryCharge < 0.5:
                print("Out of power!")
                break

    def batteryReCharge(self, charge):
        self.batteryCharge += charge
        print("Battery charge is : ", self.batteryCharge)


if __name__ == "__main__":
    r = Robot1()
    r.move(10)
    r.batteryReCharge(3.0)
    r.move(5)

