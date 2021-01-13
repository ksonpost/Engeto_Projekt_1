# Uložené proměnné
oddelovac = ('=' *80)
oddelovac2 = ('=' *40)
zadani_user = ['bob', 'ann', 'mike', 'liz']
zadani_pw = ['123', 'pass123', 'password123', 'pass123']
TEXTS1 = '''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.'''

TEXTS2 = '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''

TEXTS3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''

TEXTS_ALL = [TEXTS1, TEXTS2, TEXTS3]


TEXTS4_pocet = ['that rises sharply some', 1000, 'feet above Twin Creek Valley to an elevation of more than', 7500, 'feet above sea level. The butte is located just north of US 30N']

# 1. Na začátku přivítá uživatele.
print("Vítej v aplikaci, prosím o přihlášení!")
print(oddelovac2)

# 2. Vyžádá si od uživatele přihlašovací jméno a heslo
# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
zadej1 = str(input('Přihlašovací jméno: '))
zadej2 = str(input('Heslo: '))
print(oddelovac2)
print('Zadané přihlašovací jméno je:', zadej1 in zadani_user)
print('Zadané přihlašovací heslo je:', zadej2 in zadani_pw)
print(oddelovac2)

# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.
vyber_text = int(input('Vyber si svůj text zadáním hodnoty 1, 2, nebo 3: '))
vybrani_textu = TEXTS_ALL[vyber_text - 1]
print('Tvůj vybraný text je: ' + vybrani_textu)


# 5. Pro vybraný text spočítá následující statistiky: (počet slov ; počet slov začínajících velkým písmenem ; počet slov psaných velkými písmeny ; počet slov psaných malými písmeny ; počet čísel (ne cifer!))
print(oddelovac2)

for char in '-.,\n':
    TEXTS1=TEXTS1.replace(char,' ')
    TEXTS1=TEXTS1.lower()
pocet_slov_1 = TEXTS1.split()

if vyber_text == 1:
    print('Počet slov vybraného textu je: ',len(pocet_slov_1))

for char in '-.,\n':
    TEXTS2=TEXTS2.replace(char,' ')
    TEXTS2=TEXTS2.lower()
pocet_slov_2 = TEXTS2.split()
if vyber_text == 2:
    print('Počet slov vybraného textu je: ',len(pocet_slov_2))

for char in '-.,\n':
    TEXTS3=TEXTS3.replace(char,' ')
    TEXTS3=TEXTS3.lower()
pocet_slov_3 = TEXTS3.split()
if vyber_text == 3:
    print('Počet slov vybraného textu je: ',len(pocet_slov_3))

print(oddelovac2)




# 6.Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
# 1 * 1
# 2 *********** 11
# 3 *************** 15
# 4 ********* 9
# 5 ********** 10
#V textu, ze kterého byl vytvořen tento graf, je tedy pouze 1 jednopísmené slovo, 11 slov složených ze dvou písmen, a tak dále.




# 7. Program spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:
#"that rises sharply some 1000 feet above
#Twin Creek Valley to an elevation of more
#than 7500 feet above sea level. The butte
#is located just north of US 30N"
#text_pocet_vysledek = count(int(text_pocet))
#print(text_pocet_vysledek)