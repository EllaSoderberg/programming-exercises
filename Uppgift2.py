# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Ella Söderberg
# 12/10/2015
# Detta program printar en rondulat utifrån fyra meningar du kommer få mata in.
def instructions():
    '''Här printas instruktionerna till diktautomaten.
    '''
    print('''                DIKTAUTOMATEN''' + "\n")
    print("Skriv in fyra meningar och få ut en rondelet!" + "\n")

def poem():
    '''Här skrivs de fyra meningarna in.
    
    returns: En lista med 4 meningar.
    '''
    sentence = [None]*4
    i = 0
    while (i < 4):
        sentence[i] = input("Varsågod att skriva mening " + str(i+1) + ": ")
        i += 1
    print("\n" + "\n")
    return sentence

def poem_split(firstsentence):
    '''Delar upp första meningen i en lista.
    
    param firstsentence: Den första meningen i listan.
    returns: Orden i första meningen som en lista.
    '''
    split_sentence = firstsentence[0].split()
    return split_sentence

def poem_join(sentence_splitted):
    '''Förenar orden i listan till två egna meningar.
        
    param sentence_splitted: listan med orden som ska förenas.
    returns: primary_sentence som består av listans fyra första värden förenade och second_sentence som innehåller resten.
    '''
    primary_sentence = " ".join(sentence_splitted[:4])
    second_sentence = " ".join(sentence_splitted[4:])
    return primary_sentence, second_sentence

def poem_print(sentence1, sentence2, poemlist):
    '''Här printas dikten ut i rätt ordning.
        
    param uppercase: Gör om sentence1 till versaler och sätter den som titel. 
    param sentence1: Diktens huvudmening.
    param sentence2: Diktens andra mening. 
    param poemlist: Listan där meningarna är förvarade.
    '''
    print(sentence1.upper() + "\n")
    print(sentence1)
    print(sentence2)
    print(sentence1)
    a = 1
    while (a < 4):
        print(poemlist[a])
        a += 1
    print(sentence1)

def mainfunction():
    '''Omvandlar 4 meningar till en rondulat.
    '''
    instructions()
    sentence = poem()
    split_sentence = poem_split(sentence)
    primary_sentence, second_sentence = poem_join(split_sentence)
    poem_print(primary_sentence, second_sentence, sentence)

mainfunction()



    
