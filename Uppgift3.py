from random import *
#Visa "välkommen till nöjesfältetskylt"
#Fråga hur modig personen känner sig på en skala från 1-10 idag.
#berätta vilka attraktioner som finns ordnade efter personens modighetsnivå, perfekt, läskigare, mindre läskiga.
#Val görs, nu kör vi!
#funktion attraktion körs alternativt haveri
#Det var kul, vad vill du göra nu?
#gå därifrån

class Du:

    #Konstruktorn, initierar attributen namn, modighetsnivå och skick
    def __init__(self, dittnamn):
        self.namn = dittnamn
        self.modighetsniv = modighetsniv
        self.skick = 5

    #Visar ditt skick
    def visaskick(self):
        print("Jag ser att du just nu är ", end=" ")
        if self.skick >= 5:
            print("glad!")
        else:
            print("skrämd. Ta det lite lugnt!")
        print

    #Åka attraktion som är för läskig, skick minskar, lagom läskig, skick ökar med tre, tråkig, skick ökar med 1
    def skramd(self):
        if self.modighetsniv < magpirrfaktor:
            self.skick -= (magpirrfaktor - self.modighetsniv)
        elif self.modighetsniv == magpirrfaktor:
            self.skick += 3
        else:
            self.skick += 1

    #Äta sockervadd, skick ökar

    #Få för lågt skick, åka hem
    def illamaende(self):
        if self.skick <= 0:
            print("Nu mår du för dåligt, vi skickar hem dig nu innan något tråkigt händer. Hejdå!")

class Attraktioner:

    #Konstruktorn, initierar attributen namn, beskrivning, minimilängd, och magpirrfaktor.
    def __init__(self, attraktion, beskrivning, minimilangd, magpirrfaktor):
        self.namn = attraktion
        self.beskrivning = beskrivning
        self.minimilangd = minimilangd
        self.magpirrfaktor = magpirrfaktor
        self.dinlangd = 0

    #Visar beskrivningen utav attraktionen
    def visabeskrivning(self):
        print(self.namn, "\n", self.beskrivning, "\n", "Minimilängd: ", self.minimilangd, "\n")
        val = input("Vad vill du åka? ")
        print(val)
    #if self.dinlangd >= self.minimilangd:
#            aka()
#        else:
#            print("Du är tyvärr för kort!")

    #Kör attraktionen
    def aka(self):
        print("Då är du redo för avfärd, då startar vi " + self.namn + "!")
        crazysounds = []
        with open('crazysounds.txt', 'r', encoding="utf-8") as file:
            for sounds in file:
                crazysounds.append(sounds)
        i = 0
        while i < 4:
            print(crazysounds[round(random()*20)])
            i += 1

    #def akaigen(self):
 #       svar = input("Vill du åka något mer? ")
 #       if svar.lower().startswith("j"):

#attraktionen failar

def huvudprogram():
    dittnamn = input("Välkommen, vad heter du? ")
    dnamn = Du(dittnamn)
    dnamn.visaskick()
    modighetsniv = input("På en skala från 1-10, hur modig känner du dig idag? ")
    modig = Du(modighetsniv)
    Attraktioner("LustigaHuset", "Ett hus som e kul", 130, 1).visabeskrivning()
    Attraktioner("LustigaHuset", "Ett hus som e kul", 130, 1).aka()

huvudprogram()
