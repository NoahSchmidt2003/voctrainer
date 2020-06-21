import random
import re
import datetime





class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch

    def toString(self):
        return self.deutsch + " - " + self.englisch


play = True
askloop = True





def eingabe(filenamef, namelf):
    f = open(filenamef, 'a')
    while True:
        deutsch = input("Deutsches Wort :")
        if deutsch == "#fertig":
            return
        englisch = input(namelf + " Wort :")
        if englisch == "#fertig":
            return
        f.write(deutsch + "\n")
        f.write(englisch + "\n")
        eintraege.append(Entry(deutsch, englisch))


def abfrage(namelf):
    mistakes = 0
    correct = 0
    cstreak = 0
    csout = 0
    while True:
        n = random.randint(0, 1)
        i = random.randint(0, len(eintraege) - 1)
        if n == 0:
            tester = str(eintraege[i].englisch)
            outtester = re.sub(r"[\n\t\s]*", "", tester)
            englisch = str(input(namelf + " Übersetzung von " + eintraege[i].deutsch + ":"))
            if englisch == "#fertig":
                stop(correct, mistakes, csout, namel2)
                break

            if outtester == englisch:
                print("korrekt!")
                correct = correct + 1
                cstreak = cstreak + 1
                if cstreak >= csout:
                    csout = cstreak
            else:
                print("leider Falsch. Richtige Antwort: " + eintraege[i].englisch)
                mistakes = mistakes + 1
                cstreak = 0
        else:
            tester = str(eintraege[i].deutsch)
            outtester = re.sub(r"[\n\t\s]*", "", tester)
            deutsch = str(input("Deutsche Übersetzung von " + eintraege[i].englisch + ":"))
            if deutsch == "#fertig":
                stop(correct, mistakes, csout, namel2)
                break

            if outtester == deutsch:
                print("korrekt!")
                correct = correct + 1
                cstreak = cstreak + 1
                if cstreak >= csout:
                    csout = cstreak
            else:
                print("leider Falsch. Richtige Antwort: " + eintraege[i].deutsch)
                mistakes = mistakes + 1
                cstreak = 0


def printall():
    for eintrag in eintraege:
        print(eintrag.toString())


def load(filenamef):
    vocen = []
    vocde = []
    is_de = True
    with open(filenamef, "r") as ins:
        for line in ins:
            if is_de:
                vocde.append(line)
            else:
                vocen.append(line)
            is_de = not is_de
    x = len(vocde)
    for i in range(x):
        a = vocde[i]
        b = vocen[i]
        eintraege.append(Entry(a, b))
    print("Du hast erfolgreich deine Datei geladen")


def stop(correct, mistakes, csout, namel2f):
    print("---------------------------------------------------------------------")
    print("Du hast " + str(correct) + " Wörter richtig!")
    print("Du hast " + str(mistakes) + " Wörter falsch!")
    print("Dein höchste Streak an richtigen Wörtern beträgt " + str(csout) + " Wörter!")
    print("---------------------------------------------------------------------")
    askp = input("Willst du ins Leaderbord aufgenommen werden? y/n\n:")
    if askp == "y":
        name = input("Wie heißt du?\n:")
        l = open('recent_tests.log', 'a')
        l.write("--------------------------------------------------------------------\n")
        l.write(name + " ")
        l.write("hatte " + str(correct) + " Wörter richtig!\n")
        l.write("hatte " + str(mistakes) + " Wörter falsch!\n")
        l.write("Die höchste Streak betrug " + str(csout) + " Wörter!\n")
        l.write("Der " + namel2f + " wurde durchgeführt um : " + datetime.datetime.now().strftime("%H:%M - %d.%m.%Y\n"))
        l.write("--------------------------------------------------------------------\n")


def fr():
    global filename
    global namel
    global namel2
    global entryv
    entryv = "bonjour"
    filename = "fr_de.txt"
    namel = "Französisches"
    namel2 = "Französischtest"


def en():
    global filename
    global namel
    global namel2
    global entryv
    entryv = "hello"
    filename = "en_de.txt"
    namel = "Englische"
    namel2 = "Englischtest"


while askloop:
    askl = input("In welcher Sprache möchtest du getestet werden Französisch oder Englisch fr/en\n:")
    if askl == "fr":
        fr()
        eintraege = [Entry("hallo", entryv)]
        print("Der französische Vokabeltrainer wurde erfolgreich geladen")
        break
    elif askl == "en":
        en()
        eintraege = [Entry("hallo", entryv)]
        print("Der englische Vokabeltrainer wurde erfolgreich geladen")
        break
    else:
        print("Keine registrierte Sprache im Vokabeltrainer")

while play:
    befefehl = input("Befehl : ")
    if befefehl == "eingabe":
        eingabe(filename, namel)
    elif befefehl == "load":
        load(filename)
    elif befefehl == "abfrage":
        abfrage(namel)
        break
    elif befefehl == "stop":
        break
    elif befefehl == "ausgabe":
        printall()
    elif befefehl == "hilfe":
        print("Eine Hilfe zur Bedienung des Trainers findest du unter der readme.txt")
    else:
        print("Keine bekannte Ausgabe. Tippe: eingabe, abfrage, ausgabe, load, stop oder hilfe")

print("Bye see you later")
print("Eine Hilfe zur Bedienung des Trainers findest du unter der readme.txt")
print("Version 0.0.1")
print("©Noah.S")
