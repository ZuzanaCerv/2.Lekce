

def overeni_tel_cisla(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420"):
        return "Zadej text zpravy:"
    else:
        return False


Cislo_uzivatele = input("Zadej telefonni cislo:")




