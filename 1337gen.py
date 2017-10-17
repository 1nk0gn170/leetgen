import os
import time

def menue():
    os.system("cls")
    print("""                                               String-Tool Menü by Inkognito\n
                                                    1 - Verschlüsseln
                                                    2 - Entschlüsseln""")
    eingabe = input("\n\nNummer: ")

    if eingabe == "1":
        encrypt()

    elif eingabe == "2":
        decrypt()

    elif eingabe == "":
        menue()

    else:
        print("Ungültige Eingabe.")
        input()
        menue()


def encrypt():
    os.system("cls")

    print("\n                                                 String-Tool (verschlüsselt) by Inkognito                      ")
    print  ("\n                          Um ins Hauptmenü zurückzukehren, schreibe in der Eingabe diesen Code rein => 0000")

    s = "Du hast eine ungültige Eingabe gemacht."
    raw = input("\n\nEingabe: ")
    enc = str.maketrans("AaEeLlTtOoIiSsCc", "4433117700!!55((")
	
    if raw == "":
        print(s.translate(enc))
        input()
        encrypt()

    elif raw == "0000":
        os.system("cls")
        print("\nDu wirst ins Hauptmenü weitergeleitet...")
        time.sleep(2)
        menue()

    else:
        print("\nAusgabe: %s" % (raw.translate(enc)))
        input()
        encrypt()

def decrypt():
    os.system("cls")

    print("\n                                                 String-Tool (entschlüsselt) by Jon Doe                      ")
    print  ("\n                          Um ins Hauptmenü zurückzukehren, schreibe in der Eingabe diesen Code rein => 0000")

    s = "Du hast eine ungültige Eingabe gemacht."
    raw = input("\n\nEingabe: ")
    dec = str.maketrans("4433117700!!55((", "AaEeLlTtOoIiSsCc")

    if raw == "":
        print(s.translate(dec))
        input()
        decrypt()

    elif raw == "0000":
        os.system("cls")
        print("\nDu wirst ins Hauptmenü weitergeleitet...")
        time.sleep(2)
        menue()

    else:
        print("\nAusgabe: %s" % (raw.translate(dec)))
        input()
        decrypt()

menue()