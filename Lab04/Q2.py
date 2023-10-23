class Robot1:
    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, distance):
        count = 1
        while count <= distance:
            if self.batteryCharge == 0:
                print("Out of power!")
                break
            print(f"[{count}]")
            self.batteryCharge -= 0.5
            count += 1
        else:
            if self.batteryCharge == 0:
                print("Out of power!")

    def batteryReCharge(self, charge):
        self.batteryCharge += charge
        print("Battery charge is : ", self.batteryCharge)


if __name__ == "__main__":
    r = Robot1()
    r.move(10)
    r.batteryReCharge(3.0)
    r.move(5)

