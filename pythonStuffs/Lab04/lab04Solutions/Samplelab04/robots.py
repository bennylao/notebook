import random


class Robot1:
    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, distance):

        for i in range(distance + 1):
            if self.batteryCharge < 0.5:
                print('Out of power!')
                return
            else:
                self.batteryCharge -= 0.5
                print(i)
                continue

        print(f'Robot has moved {distance} units!')
        return

    def recharge(self, charge):
        """ Recharges the robot's battery."""

        self.batteryCharge += charge
        return self.batteryCharge


class Robot2(Robot1):
    """
    Robot version 2 that inherits from version 1 adding the functionality of speaking.
    """

    def __init__(self):
        super().__init__()
        self.sayings = []

    def set_sayings(self, string_list):
        self.sayings += string_list
        return

    def speak(self):
        return print(self.sayings[random.randint(0, len(self.sayings)-1)])


r2 = Robot2()
u1 = ["Exterminate, Exterminate!", "I obey!", "You cannot escape.", "Robots do not feel fear.", "The Robots must survive!" ]
r2.set_sayings(u1)
r2.speak()

