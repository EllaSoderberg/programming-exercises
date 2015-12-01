import random
class attraktion:
    """docstring for attraktion"""
    def __init__(self, namn, magpirr):
        self.namn = namn
        self.magpirr = magpirr

    def __str__(self):
        return 'vill du åka' + self.namn + 'med magpirrsfaktorn' + self.magpirr + '?'

    def aka(self):
        print("Då är du redo för avfärd, då startar vi " + self.namn + "!")
        crazysounds = open('crazysounds.txt', 'r')
        i = 0
        while i < 4:
            print('wiho')
            i += 1

hej = attraktion('Karusell', '3')
aka()

