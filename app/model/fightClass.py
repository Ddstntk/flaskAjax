import random


class attack():
    def __init__(self, power, speed):
        self.power = power #1-100
        self.speed = speed  #1-100


class defence():
    def __init__(self, speed, efficacy):
        self.speed = speed # 1-100
        self.efficacy = efficacy # 1-100


class rest():
    def __init__(self):
        self.rest = 1


class fight():
    def __init__(self, fighterA, fighterB, actionList=[]):
        self.FighterA = fighterA
        self.FighterB = fighterB
        self.actionList = []

    def addAction(self, action):
        self.actionList.append(action)

        if len(self.actionList) > 1:
            print("wywołuję kill and win")
            self.killAndWin()

    def dupadupa(self):
        print(self.actionList)

    def killAndWin(self):
        print("Zaczynajo walczyć!")

        actionA = self.actionList[0]
        actionB = self.actionList[1]
        print(self.FighterA, self.actionList[0])
        print(self.FighterB, self.actionList[1])

        print("Walczo!")

        if isinstance(actionA, attack):
            print("wykryłem atak")
            if isinstance(actionB, attack):                                                           # obaj atakują
                self.FighterA.health -= int(actionA.power * (random.randrange(7, 13))/10)
                self.FighterB.health -= int(actionB.power * (random.randrange(7, 13)/10))
                print(self.FighterA.health, self.FighterB.health)

            elif isinstance(actionB, defence):                                                        # A atak B obrona
                speedDiff = actionA.speed - actionB.speed
                if speedDiff < -50:
                    chanceFactor = (speedDiff + 100)/2
                    chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
                    if chanceFactor > -45:
                        self.FighterA.health -= int(actionA.power * (random.randrange(7, 13)/10) * 100/actionB.efficacy)

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75
                self.FighterB.health -= int(actionA.power * (random.randrange(7, 13)/10))

        elif isinstance(actionA, defence):                                                           # A obrona B atak
            print("wykryłem obronę")

            if isinstance(actionB, attack):
                speedDiff = actionB.speed - actionA.speed
                if speedDiff < -50:
                    chanceFactor = (speedDiff + 100) / 2
                    chanceFactor += int(chanceFactor * (random.randrange(8, 18)/10))
                    if chanceFactor > -45:
                        self.FighterB.health -= int(actionB.power * (random.randrange(7, 13)/10) * 100 / actionA.efficacy)

            elif isinstance(actionB, defence):                                                       # Obaj się bronią
                pass

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75

        elif isinstance(actionA, rest):
            print("wykryłem odpoczynek")
            if isinstance(actionB, attack):                                                           # obaj atakują
                self.FighterA.health -= int(actionB.power * (random.randrange(7, 13))/10)
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75
                print(self.FighterA.health, self.FighterB.health)

            elif isinstance(actionB, defence):                                                        # A atak B obrona
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75

            elif isinstance(actionB, rest):                                                        # A atak B obrona
                if self.FighterA.stamina < 550:
                    self.FighterA.stamina += 75
                if self.FighterB.stamina < 550:
                    self.FighterB.stamina += 75

        self.actionList = []
