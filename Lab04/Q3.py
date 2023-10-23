import random

from Lab04.Q2 import Robot1


class Robot2(Robot1):
    def __init__(self, ):
        super().__init__()
        self.sayings = ["default1", "default2", "default3"]

    def setSayings(self, sentences_list):
        self.sayings = sentences_list

    def speak(self):
        print(random.choice(self.sayings))
