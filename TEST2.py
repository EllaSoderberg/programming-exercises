class Attraktioner:

    #Konstruktorn, initierar attributen namn, beskrivning, minimilängd, och magpirrfaktor.
    def __init__(self, attraktion, beskrivning, minimilangd, magpirrfaktor):
        self.namn = attraktion
        self.beskrivning = beskrivning
        self.minimilangd = minimilangd
        self.magpirrfaktor = magpirrfaktor
        self.dinlangd = 0

def visabeskrivning():
    for attraktion in Attraktioner:
        print(attraktion, "\n", beskrivning, "\n", "Minimilängd: ", minimilangd, "\n")
    val = input("Vad vill du åka? ")
    print(val)

def info():
    print("skriv tre attraktioner du vill ha")
    attraktion = [None]*3
    i = 0
    while i < 3:
        attraktion = input("Vad heter attraktionen? ")
        i += 1
    visabeskrivning()

info()
