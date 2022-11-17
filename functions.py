from fileHandling import loadData



def TortenelemMenu():
    option = -1
    while option < 1 or option > 6:
        print('1 - Hány éve szerepelnek')
        print('2 - Legeredményesebb szezon')
        print('3 - Leggyengébb szezon')
        print('4 - Legtöbb lőtt gól a szezonban')
        print('5 - Eddigi Top 3 szezonok')
        print('6 - Szezonlekérés')
        print('7 - Vissza a főmenübe')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def SzezonbeliMeccsek():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def Jegyvasarlas():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def Jegyeim():
    option = -1
    while option < 1 or option > 6:
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        print('6 - ')
        print('7 - ')
        option = int(input('Válasszon a fentiek közül: '))
    return option

def MainMenu():
    option = -1
    while option < 1 or option > 5:
        print('1 - Klubtörténelem')
        print('2 - Szezonbeli meccsek')
        print('3 - Jegyvásárlás')
        print('4 - Jegyeim')
        print('5 - Kilépés')


        option = int(input('Válasszon a fentiek közül: '))
    return option


def OsszesSzereples(data):
    return(len(data))

#regisztracio
def login():    
    user = input("Felhasználónév: ")
    passw = input("Jelszó: ")
    f = open("login_projekt/users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (user in us) and (passw in pw):
            print ("Login successful!")
            return True
    print ("Hibás felhasználónév/jelszó")
    return False

def signup():
    file = open('login_projekt/users.txt', 'a', encoding='utf-8')
    username = input('Új felhasználónév: ')
    password = input('Új jelszó: ')
    term = input('szerződés(y/n): ')
    if term == 'y':
        print('regisztráció sikeres!')
        file.write(f'{username}|{password}\n')
    elif term == 'n':
        print('Sikertelen regisztráció!')
    else:
        print('nincs ilyen opció!')


def main():
    choice = input('a) login b) sign up ')
    if choice == 'a':
        log = login()
        if log == True:
            # menü
            pass
    elif choice == 'b':
            signup()
            main()
    else: print('nincs ilyen opció')
#regisztracio vege
