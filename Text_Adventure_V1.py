#Libraries
import random
import os
import time

#Bool Variables
choice = False
Priority = False

#Int Variables
spellDamage = 0
numEnemies = 1

#Defining Functions
def clear():        #<-- Clears the console
    os.system('cls')
def wait(a):        #<-- Creates a custom delay In the code
    time.sleep(a)
def certainty(a):   #<-- Asks the player If they're sure they want to do something
    global choice
    choosing = input(a + " [Y/N]\n---> ")
    if choosing.lower() == "y" or choosing.lower() == "yes":
        choice = True
    elif choosing.lower() == "n" or choosing.lower() == "no":
        choice = False
    else:
        clear()
        print("Invalid Input")
        wait(1)
        clear()
        certainty(a)     
def makeCard(a):    #<-- Creates a card that shows a character's stats
    CardBorders = "===================================="
    Card1dgSpacing = ["|| HP: " + str(a[0]) + "                          ||", "|| MP: " + str(a[1]) + "                          ||", "|| AP: " + str(a[2]) + "                          ||", "|| WP: " + str(a[3]) + "                          ||", "|| SPD: " + str(a[4]) + "                         ||"]
    Card2dgSpacing = ["|| HP: " + str(a[0]) + "                         ||", "|| MP: " + str(a[1]) + "                         ||", "|| AP: " + str(a[2]) + "                         ||", "|| WP: " + str(a[3]) + "                         ||", "|| SPD: " + str(a[4]) + "                        ||"]
    index = 0
    stat = 0
    last = len(a) - 2
    print(CardBorders)
    print(a[5])
    print(CardBorders)
    while index < last:
        if len(str(a[stat])) == 1:
            print(Card1dgSpacing[stat])
            stat += 1
            index += 1
        elif len(str(a[stat])) == 2:
            print(Card2dgSpacing[stat])
            index += 1
            stat += 1
    print(CardBorders)
def invalidInput():
    clear()
    print("Invalid input")
    wait(1)
    clear()

#Dice
diceVal = 0
def d4Roll():  #<-- Rolls a 4 faced dice
    global diceVal
    diceVal = random.randrange(1,4)
def d6Roll():  #<-- Rolls a 6 faced dice
    global diceVal
    diceVal = random.randrange(1,6)
def d20Roll(): #<-- Rolls a 20 faced dice
    global diceVal
    diceVal = random.randrange(1,20)

#===== Characters =====

#ClassName:         Simboliza o Nome do Personagem ou Monstro
#Hit-Points (Hp):   Simboliza a quantidade de vida o personagem tem até ficar inconsciente
#Mana-Points (Mp):  Simboliza o recurso utilizado para criar e lançar feitiços
#Armor Points (Ap): Simboliza a quantidade de dano que é subtraído após um ataque
#Weapon (Wp):       Simboliza a quantidade de dano que este personagem faz após um ataque
#Initiative (Init): Simboliza a rapidez que este personagem tem em fazer uma acção

#======= Allies =======
#==== Warrior Stats ===
WStats = [32, 5, 2, 5, 2, "||            Warrior             ||", "Warrior"]
#Index: 0 = Hp, 1 = Mp, 2 = Ap, 3 = Wp, 4 = Init, 5 = Name
#Warrior Spell (Rushdown)
#Rushdown 
warriorSpell = ["Rushdown"]
warriorSpellDesc = ["You use magic to enhance your speed and tackle your foe to maximize impact. (Costs 5 Mana)"]
def Rushdown():
    global spellDamage
    d4Roll()
    spellDamage = -1 * (WStats[3] + diceVal)
    WStats[2] = 5


#==== Priest Stats ====
PStats = [20, 25, 0, 2, 6, "||             Priest             ||", "Priest"]
#Index: 0 = Hp, 1 = Mp, 2 = Ap, 3 = Wp, 4 = Init, 5 = Name
#Priest Spells (Exorcism & Mend)
#Exorcism (Apply on Enemy) [roll 4 faced dice]
P1SpellEffectValue = -1 * (diceVal * 2)
P1SpellMPCost = 5
#Mend (Apply on ally) [roll 6 faced dice]
P2SpellEffectValue = (diceVal + PStats[3])
P2SpellMPCost = 3

#====== Enemies ========
#== Orc Warrior Stats ==
OWStats = [15, 0, 2, 2, 2, "||           Orc Warrior          ||" ,"Orc Warrior"]
#Index: 0 = Hp, 1 = Mp, 2 = Ap, 3 = Wp, 4 = Init, 5 = Card name, 6 = Enemie name

#= Character Selection =
def CharSelect():
    clear()
    print("Welcome adventurer!")
    global pStats
    global pClass
    pClass = input("Choose the class you'd like to play as:\n1-> Warrior\n2-> Priest\n---> ")
    if pClass == "1" or pClass.lower() == "warrior":
        clear()
        makeCard(WStats)
        certainty("Are you sure you want to play as a Warrior?")
        if choice == True:
            pStats = WStats
            pClass = WStats[6]
        else:
            clear()
            CharSelect()   
    elif pClass == "2" or pClass.lower() == "priest":
        clear()
        makeCard(PStats)
        certainty("Are you sure you want to play as a Priest?")
        if choice == True:
            pStats = PStats
            pClass = PStats[6]
        else:
            clear()
            CharSelect()  
    else:
        invalidInput()
        CharSelect()

#=== Combat System ====
#== Initiative Phase ==
def initPhase(a, b):
    global Priority
    d20Roll()
    print(diceVal)
    pOrder = diceVal + a[4]
    d20Roll()
    print(diceVal)
    eOrder = diceVal + b[4]
    if pOrder < eOrder:
        Priority = False
    elif pOrder > eOrder:
        Priority = True
    else:
        if a[4] > b[4]:
            Priority = True
        else:
            Priority = False
    print(Priority)

#==== Action Phase ====
def actionPhase(a, b):
    clear()
    if Priority == True:
        print("An " + b[6] + " is standing in your way") #<-- Says name of enemy
        attack = input("What will you do?\n1-> Use a Physical attack\n2-> Use Magic\n---> ")
        if attack == "1":
            dmg = a[3] - b[2]
            if dmg <= 0:
                dmg = 0
            b[0] = b[0] - dmg
            print("You atacked the " + b[6] + " with all your might, dealing " + str(dmg) + " points of damage!")
            if b[0] <= 0:
                print(b[5] + " has perished.")
        elif attack == "2" and pClass == "Warrior":
            mana = a[1]
            clear()
            spell = input("Current Mana: " + str(mana) + "\nSpells\n1-> Rushdown: You use magic to enhance your speed and tackle your foe to maximize impact. (Costs 5 Mana)\n2-> Exit spells menu\n---> ")
            if spell == "1" and mana >= 5:
                Rushdown()
                mana -= 5
                print(spellDamage)
            elif spell == "1" and mana < 5:
                clear()
                print("Not enough mana")
                wait(1)
                clear()

    else:
        print("placeholder")

CharSelect()
initPhase(pStats, OWStats)
actionPhase(pStats, OWStats)