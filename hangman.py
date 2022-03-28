import random


class Game:
    gracze = 0
    poziom = 0
    zycia = 0
    haslo = ""
    haslowynik =""

    atlas = ["konwalia", "cytryna", "bakłażan", "pieczarki", "grzybnia", "burza", "huragan", "tajfun", "powódź", "lawina", "próżnia",
    "głupota", "mądrość", "chytrość", "przebiegłość", "inteligencja", "pantera", "mrówka", "kangur", "nosorożec",
    "pielęgniarka", "wykładowca", "murarz", "pisarka", "sąsiad", "braciszek",
    "stół", "podłoga", "krzesiwo", "zegarek", "nożyce", "liść", "pióropusz", "piec"]
    def _Play(self):
        print("Playing")
        if(self.gracze==1): 
            print("Tryb jednoosobowy")
            self.haslo = self.atlas[random.randint(0,len(self.atlas))]

            print(self.haslo) 

            for a in self.haslo:
                self.haslowynik = self.haslowynik + "_"
            print("HASŁO: "+ self.haslowynik)
            licznik = 0
            while True:
                if(self.haslo==self.haslowynik):
                    print("WYGRANA")
                    break
                if(self.zycia==0):
                    print("PRZEGRANA")
                    break
                literka=""
                while True:
                    try:
                        a = str(input("Podaj litere: "))
                        if(len(a)==1 and a not in self.haslowynik):
                            print()
                        else:
                            raise ValueError('Błąd')
                    except ValueError:
                        print("Błąd!!!")
                        continue
                    else:
                        literka=a
                        break
                licznik_literki = 0
                licznik_bledu = True
                newhaslo = []
                for a in self.haslo:
                    if(a==literka.lower()):
                        newhaslo.append(a)
                        licznik_bledu = False
                    else:
                        if(self.haslo[licznik_literki]==self.haslowynik[licznik_literki]):
                            newhaslo.append(self.haslo[licznik_literki])
                        else:
                            newhaslo.append("_")
                    licznik_literki = licznik_literki + 1
                newhaslostr = ""
                for s in newhaslo:
                    newhaslostr = newhaslostr + s
                self.haslowynik = newhaslostr
                if(licznik_bledu):
                        self.zycia = self.zycia-1
                        print("życia: "+ str(self.zycia))
                print("HASŁO: " + self.haslowynik)



        if(self.gracze==2): 
            print("Tryb dwuosobowy")
            while True:
                try:
                    a = str(input("Niech jeden z graczy poda hasło: "))
                    if(len(a)>1 and str.isalpha(a)):
                        print()
                    else:
                        raise ValueError('Błąd')
                except ValueError:
                    print("Błąd!!!")
                    continue
                else:
                    self.haslo=a.lower()
                    break

            print(self.haslo) 

            for a in self.haslo:
                self.haslowynik = self.haslowynik + "_"
            print("HASŁO: "+ self.haslowynik)
            licznik = 0
            while True:
                if(self.haslo==self.haslowynik):
                    print("WYGRANA")
                    break
                if(self.zycia==0):
                    print("PRZEGRANA")
                    break
                literka=""
                while True:
                    try:
                        a = str(input("Podaj litere: "))
                        if(len(a)==1 and a not in self.haslowynik):
                            print()
                        else:
                            raise ValueError('Błąd')
                    except ValueError:
                        print("Błąd!!!")
                        continue
                    else:
                        literka=a
                        break
                licznik_literki = 0
                licznik_bledu = True
                newhaslo = []
                for a in self.haslo:
                    if(a==literka.lower()):
                        newhaslo.append(a)
                        licznik_bledu = False
                    else:
                        if(self.haslo[licznik_literki]==self.haslowynik[licznik_literki]):
                            newhaslo.append(self.haslo[licznik_literki])
                        else:
                            newhaslo.append("_")
                    licznik_literki = licznik_literki + 1
                newhaslostr = ""
                for s in newhaslo:
                    newhaslostr = newhaslostr + s
                self.haslowynik = newhaslostr
                if(licznik_bledu):
                        self.zycia = self.zycia-1
                        print("życia: "+ str(self.zycia))
                print("HASŁO: " + self.haslowynik)

    def __init__(self):
        print(self)

    def poziom(self):
        while True:
            try:
                a = int(input("Podaj poziom od 1 do 3: 1 - łatwy, 2 - średni, 3 - trudny: "))
                if(a == 1 or a==2 or a==3):
                    print()
                else:
                    raise ValueError('Błąd')
            except ValueError:
                print("Błędny poziom!!!")
                continue
            else:
                self.poziom = a
                if(a==1):
                    self.zycia = 8
                    print("Wybrany poziom: Łatwy")
                if(a==2):
                    self.zycia = 5
                    print("Wybrany poziom: Średni")
                if(a==3):
                    self.zycia = 3
                    print("Wybrany poziom: Trudny")
                break

    def liczba_graczy(self):
        while True:
            try:
                a = int(input("Podaj liczbe graczy: "))
                if(a == 1 or a==2):
                    print()
                else:
                    raise ValueError('Błąd')
            except ValueError:
                print("Błędna liczba graczy!!!")
                continue
            else:
                self.gracze = a
                print("Liczba graczy: "+str(a))
                break

    def logo(self):
        print(" _                                             ")
        print("| |                                            ")
        print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
        print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
        print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
        print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
        print("                    __/ |                      ")
        print("                   |___/  ")
        print("      ___________.._______")
        print("     | .__________))______|")
        print("     | | / /      ||")
        print("     | |/ /       ||")
        print("     | | /        ||.-.-.")
        print("     | |/         |/  _  \ ")
        print("     | |          ||  ./,|")
        print("     | |          (\\._..")
        print("     | |         .----..")
        print("     | |        /Y . . Y\ ")
        print("     | |       // |   | \\ ")
        print("     | |      //  | . |  \\ ")
        print("     | |     .)   |   |   (. ")
        print("     | |          ||.|| ")
        print("     | |          || ||")
        print("     | |          || ||")
        print("     | |          || || ")
        print("     | |         / | | \ ")
        print("     ----------|_`-| `-| |---|")
        print()
        print()
        print()



class Hangman(Game):
    def test(self):
        print("test")

    def __init__(self):
        self.logo()
        self.poziom()
        self.liczba_graczy()
        self._Play()



H1 = Hangman()