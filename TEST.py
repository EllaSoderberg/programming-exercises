

    #Konstruktorn, initierar attributen namn, beskrivning, minimilängd, och magpirrfaktor.
def hej(self, attraktion, beskrivning, minimilangd, magpirrfaktor):
    self.namn = attraktion
    self.beskrivning = beskrivning
    self.minimilangd = minimilangd
    self.magpirrfaktor = magpirrfaktor

def visabeskrivning(self, dinlangd):
    print(self.namn, "\n", self.beskrivning, "\n", "Minimilängd: ", self.minimilangd, "\n")
    val = input("Vad vill du åka? ")
    if dinlangd >= self.minimilangd:
        aka()
    else:
        print("Du är tyvärr för kort!")
        
def aka(self):
    print("Då är du redo för avfärd, då startar vi " + self.namn + "!")
    crazysounds = open('crazysounds.txt', 'r')
    i = 0
    while i < 4:
        print(crazysounds[random.randrange(0, 20)])
        i += 1

LustigaHuset = hej("LustigaHuset", "Ett hus som e kul", 130, 1)
visabeskrivning(140)
aka()

