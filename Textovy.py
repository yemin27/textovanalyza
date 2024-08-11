"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Yegor Gladush
email: ygladush@seznam.cz
discord: yegi95
"""

# Registrované uživatele
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Vyžádání uživatelského jména a hesla
jmeno = input("jmeno: ")
heslo = input("heslo: ")

# Ověření zadaných údajů
if jmeno in uzivatele and uzivatele[jmeno] == heslo:
    print(f"----------------------------------------\nVítej v textovém analyzátoru, {jmeno}\nMáme pro tebe 3 různé texty pro analýzu.\n----------------------------------------")
else:
    print("Neregistrovaný uživatel, vypínám program")
    exit()

# Texty pro analýzu
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Vyžádání čísla textu
try:
    vyberTextu = int(input("Zadej číslo od 1 do 3 pro výběr textu: "))
    if vyberTextu not in range(1, 4):
        print("Nesprávná volba, ukončení programu.")
        exit()
except ValueError:
    print("Chybný vstup, ukončení programu.")
    exit()

# Volba textů
zvolenyText = TEXTS[vyberTextu - 1]

# Rozdělení textu na slova
slova = zvolenyText.split()

# Počet slov
pocetSlov = len(slova)

# Počet slov začínajících velkým písmenem
zahlavniPismena = sum(1 for slovo in slova if slovo.istitle())

# Počet slov psaných velkým písmenem
velkaPismena = sum(1 for slovo in slova if slovo.isupper() and slovo.isalpha())

# Počet slov psaných malými písmeny
malaPismena = sum(1 for slovo in slova if slovo.islower())

# Počet čísel v textu
ciselneRady = sum(1 for slovo in slova if slovo.isdigit())

# Součet všech čísel v textu
sumaCisel = sum(int(slovo) for slovo in slova if slovo.isdigit())

# Výstup
print(f"----------------------------------------\nZvolený text obsahuje {pocetSlov} slov.")
print(f"Tady je {zahlavniPismena} zahlavních písmen")
print(f"Tady je {velkaPismena} slov psaných velkým písmenem.")
print(f"Tady je {malaPismena} slov s malým písmenem.")
print(f"Tady je {ciselneRady} čísel.")
print(f"Suma všech čísel: {sumaCisel}\n----------------------------------------")

# Sloupcový graf
delkaSlov = [len(slovo.strip(",.")) for slovo in slova]
delkaPocet = {}

for delka in delkaSlov:
    delkaPocet[delka] = delkaPocet.get(delka, 0) + 1

print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
for delka in sorted(delkaPocet):
    print(f"{delka:>3}|{'*' * delkaPocet[delka]:<13}|{delkaPocet[delka]}")