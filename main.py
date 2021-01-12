oddelovac = ('=' *80)
oddelovac2 = ('=' *40)
zadani_user = ['bob', 'ann', 'mike', 'liz']
zadani_pw = ['123', 'pass123', 'password123', 'pass123']

# Na začátku přivítá uživatele.
print("Vítej v aplikaci, prosím o přihlášení!")
print(oddelovac2)

# Vyžádá si od uživatele přihlašovací jméno a heslo
# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

zadej1 = str(input('Přihlašovací jméno: '))
zadej2 = str(input('Heslo: '))
print(oddelovac2)
print('Zadané přihlašovací jméno je:', zadej1 in zadani_user)
print('Zadané přihlašovací heslo je:', zadej2 in zadani_pw)
print(oddelovac2)


# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.




# Pro vybraný text spočítá následující statistiky:
#- počet slov,
#- počet slov začínajících velkým písmenem,
#- počet slov psaných velkými písmeny,
#- počet slov psaných malými písmeny,
#- počet čísel (ne cifer!).




# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
# 1 * 1
# 2 *********** 11
# 3 *************** 15
# 4 ********* 9
# 5 ********** 10
#V textu, ze kterého byl vytvořen tento graf, je tedy pouze 1 jednopísmené slovo, 11 slov složených ze dvou písmen, a tak dále.




# Program spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:
#"that rises sharply some 1000 feet above
#Twin Creek Valley to an elevation of more
#than 7500 feet above sea level. The butte
#is located just north of US 30N"




