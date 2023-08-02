
def nauja_partija():
    from main import zaidimas
    zaidejo_noras = input("Norite naujos partyjos? Y \ N ?")
    if zaidejo_noras == 'Y' or zaidejo_noras == 'y':
        a = ['7', '8', '9']
        b = ['4', '5', '6']
        c = ['1', '2', '3']
        for x in a, b, c:
            print(x)
        return zaidimas()
    if zaidejo_noras == 'N' or zaidejo_noras == 'n':
        print('Programa baige darba iki :-) ')
        return False
    else:
        print("Ivedei negalima simboli galimi variantai Y,y,N,n")
        nauja_partija()