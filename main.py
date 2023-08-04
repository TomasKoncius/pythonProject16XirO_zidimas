import nauja_partija

# ('Zaidejas X pasirinkimas: ')))
def tikrinimas1():

    if pasirinkimas1_zaidejo_X in a:
        a[a.index(pasirinkimas1_zaidejo_X)] = zaidejas1
        return pasirinkimas1_zaidejo_X
    elif pasirinkimas1_zaidejo_X in b:
        b[b.index(pasirinkimas1_zaidejo_X)] = zaidejas1
        return pasirinkimas1_zaidejo_X
    elif pasirinkimas1_zaidejo_X in c:
        c[c.index(pasirinkimas1_zaidejo_X)] = zaidejas1
        return pasirinkimas1_zaidejo_X
    else:
        print('Neteisingas pasirinkimas')


# Tikrina O
def Laimi_O():
    # from main_pagrindinis import a, b, c
    if a[0] == 'O' and b[1] == 'O' and c[2] == 'O' or a[2] == 'O' and b[1] == 'O' and c[0] == 'O' or a[0] \
            == 'O' and a[1] == 'O' and a[2] == 'O' or b[0] == 'O' and b[1] == 'O' and b[2] == 'O' or c[0] \
            == 'O' and c[1] == 'O' and c[2] == 'O' or a[0] == 'O' and b[0] == 'O' and c[0] == 'O' or a[1] \
            == 'O' and b[1] == 'O' and c[1] == 'O' or a[2] == 'O' and b[2] == 'O' and c[2] == 'O':
        print("Zaidejas uz O laimejo ")
        return True


# tikrina X
def LaimiX():
    # from main_pagrindinis import a, b, c
    if a[0] == 'X' and b[1] == 'X' and c[2] == 'X' or a[2] == 'X' and b[1] == 'X' and c[0] == 'X' or a[0] \
            == 'X' and a[1] == 'X' and a[2] == 'X' or b[0] == 'X' and b[1] == 'X' and b[2] == 'X' or c[0] \
            == 'X' and c[1] == 'X' and c[2] == 'X' or a[0] == 'X' and b[0] == 'X' and c[0] == 'X' or a[1] \
            == 'X' and b[1] == 'X' and c[1] == 'X' or a[2] == 'X' and b[2] == 'X' and c[2] == 'X':
        print("Zaidejas uz X laimejo ")
        return True

# Tikrinama ar lygiosios
def Lygioios():
    # from main_pagrindinis import a, b, c
    if a[0] == 'X' and a[1] == 'O' and a[2] == 'O' and b[0] == 'O' and b[1] == 'X' and b[2] == 'X' and c[0] \
            == 'X' and c[1] == 'X' and c[2] == 'O' or a[0] == 'O' and a[1] == 'O' and a[2] == 'X' and b[0] \
            == 'X' and b[1] == 'X' and b[2] == 'O' and c[0] == 'O' and c[1] == 'X' and c[2] == 'X' or a[0] \
            == 'O' and a[1] == 'X' and a[2] == 'O' and b[0] == 'X' and b[1] == 'O' and b[2] == 'X' \
            and c[0] == 'X' and c[1] == 'O' and c[2] == 'X' or a[0] == 'O' and a[1] == 'X' and a[2] \
            == 'X' and b[0] == 'X' and b[1] == 'O' and b[2] == 'O' and c[0] == 'X' and c[1] == 'X' \
            and c[2] == 'O' or a[0] == 'X' and a[1] == 'X' and a[2] == 'O' and b[0] == 'X' and b[1] == \
            'O' and b[2] == 'O' and c[0] == 'O' and c[1] == 'X' and c[2] == 'X' or a[0] == 'O' and a[1] \
            == 'X' and a[2] == 'X' and b[0] == 'O' and b[1] == 'O' and b[2] == 'X' and c[0] == 'X' and c[1] \
            == 'X' and c[2] == 'O' or a[0] == 'X' and a[1] == 'O' and a[2] == 'O' and b[0] == 'O' and b[1] \
            == 'X' and b[2] == 'X' and c[0] == 'X' and c[1] == 'X' \
            and c[2] == 'O' or a[0] == 'X' and a[1] == 'O' and a[2] \
            == 'X' and b[0] == 'O' and b[1] == 'O' and b[2] == 'X' and c[0] == 'X' and c[1] == 'X' \
            and c[2] == 'O' or a[0] == 'X' and a[1] == 'X' and a[2] \
            == 'O' and b[0] == 'O' and b[1] == 'O' and b[2] == 'X' and c[0] == 'X' and c[1] == 'O' \
            and c[2] == 'X' or a[0] == 'X' and a[1] == 'X' and a[2] \
            == 'O' and b[0] == 'O' and b[1] == 'X' and b[2] == 'X' and c[0] == 'X' and c[1] == 'O' \
            and c[2] == 'O' or a[0] == 'O' and a[1] == 'X' and a[2] \
            == 'X' and b[0] == 'X' and b[1] == 'X' and b[2] == 'O' and c[0] == 'O' and c[1] == 'O' \
            and c[2] == 'X' or a[0] == 'O' and a[1] == 'X' and a[2] \
            == 'X' and b[0] == 'X' and b[1] == 'O' and b[2] == 'O' and c[0] == 'X' and c[1] == 'O' \
            and c[2] == 'X ' or a[0] == 'X' and a[1] == 'O' and a[2] \
            == 'X' and b[0] == 'X' and b[1] == 'O' and b[2] == 'X' and c[0] == 'O' and c[1] == 'X' \
            and c[2] == 'O' or a[0] == 'X' and a[1] == 'O' and a[2] \
            == 'X' and b[0] == 'X' and b[1] == 'O' and b[2] == 'X' and c[0] == 'O' and c[1] == 'X' \
            and c[2] == 'O' or a[0] == 'O' and a[1] == 'X' and a[2] \
            == 'O' and b[0] == 'X' and b[1] == 'X' and b[2] == 'O' and c[0] == 'X' and c[1] == 'O' \
            and c[2] == 'X':
        print("LYGIOSIOS ")
        return True


# neveikianti logika "tikrinti_lygiasias(a, b, c)"
# def tikrinti_lygiasias(a, b, c):
#     if '1' not in a and '2' not in a and '3' not in a and '4' not in a and '5' not in a and '6' not in \
#             a and '7' not in a and '8' not in a and '9' not in a:
#         print('Lygiosios')


def tikrinimas2():
    if pasirinkimas2_zaidejo_O in a:
        a[a.index(pasirinkimas2_zaidejo_O)] = zaidejas2
        return pasirinkimas2_zaidejo_O
    elif pasirinkimas2_zaidejo_O in b:
        b[b.index(pasirinkimas2_zaidejo_O)] = zaidejas2
        return pasirinkimas2_zaidejo_O
    elif pasirinkimas2_zaidejo_O in c:
        c[c.index(pasirinkimas2_zaidejo_O)] = zaidejas2
        return pasirinkimas2_zaidejo_O
    else:
        print('Neteisingas pasirinkimas')
        # str(input(tikrinimas2('Zaidejas O pasirinkimas: ')))
pasirinkimas1_zaidejo_X = ''
pasirinkimas2_zaidejo_O = ''

# Kintamieji + Masyvai
zaidejas1 = 'X'
zaidejas2 = 'O'
a = ['7', '8', '9']
b = ['4', '5', '6']
c = ['1', '2', '3']
for x in a, b, c:
    print(x)
zaidejo_noras = ''
def isvalo():
    global a, b, c
    a = ['7', '8', '9']
    b = ['4', '5', '6']
    c = ['1', '2', '3']


def zaidimas():
    isvalo()
    while True:
        # zaidimukas su tikrinimu ir stabdymu)
        global pasirinkimas1_zaidejo_X
        pasirinkimas1_zaidejo_X = str(input('Zaidejas X pasirinkimas: '))
        tikrinimas1()
        for x in a, b, c:
            print(x)

        if LaimiX() == True:
            nauja_partija.nauja_partija(zaidejo_noras=input("Norite naujos partyjos? Y \ N ?"))
            break

        elif Lygioios() == True:
            nauja_partija.nauja_partija(zaidejo_noras = input("Norite naujos partyjos? Y \ N ?"))
            break

        elif Laimi_O() == True:
            nauja_partija.nauja_partija(zaidejo_noras = input("Norite naujos partyjos? Y \ N ?"))
            break
        global pasirinkimas2_zaidejo_O
        pasirinkimas2_zaidejo_O = str(input('Zaidejas O pasirinkimas: '))
        tikrinimas2()
        for x in a, b, c:
            print(x)

        if Laimi_O() == True:
            nauja_partija.nauja_partija(zaidejo_noras = input("Norite naujos partyjos? Y \ N ?"))
            break

        elif LaimiX() == True:
            nauja_partija.nauja_partija(zaidejo_noras = input("Norite naujos partyjos? Y \ N ?"))
            break

        elif Lygioios() == True:
            nauja_partija.nauja_partija(zaidejo_noras = input("Norite naujos partyjos? Y \ N ?"))
            break
if __name__ == "__main__":
    zaidimas()
