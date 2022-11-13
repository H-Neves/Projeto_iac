#=========== Libraries ===========
import random
import time
import curses

#=========== Base function ===========
def wait(a):
    time.sleep(a)

#=========== Dice ===========
#- Int variable:
diceVal = 0

#- Functions:
def d4Roll():  #<-- Rolls a 4  faced dice
    global diceVal
    diceVal = random.randrange(1,4) #<-- asks for a random number from 1 to 4 and atributes it to the int variable

def d6Roll():  #<-- Rolls a 6  faced dice
    global diceVal
    diceVal = random.randrange(1,6) #<-- asks for a random number from 1 to 6 and atributes it to the int variable

def d20Roll(): #<-- Rolls a 20 faced dice
    global diceVal                   
    diceVal = random.randrange(1,20) #<-- asks for a random number from 1 to 20 and atributes it to the int variable

#=========== Characters ===========
#- Allie's' lists:
warrior_stats = ['32','0', '2', '5', '2', "||            Warrior             ||", "Warrior"]
priest_stats  = ['0', '0', '0', '2', '6', "||            Priest              ||", "Priest" ]
#Lists Index: 0 = Hp, 1 = Mp, 2 = Ap, 3 = Wp, 4 = Init, 5 = Card Name, 6 = Class name

#- Allies's Int Variables:
warrior_selected_attack = 0
#Index: 1 = physical, 2 = Rushdown
priest_selected_attack = 2
#Index: 1 = physical, 2 = Exorcism, 3 = Mend

#- Allie's attacks functions:
#=========== Warrior ===========
#- Attack choice:
def warrior_attacks():
    if warrior_selected_attack == 1:
        physicalAttack(warrior_stats, targets[0])

    elif warrior_selected_attack == 2:
        Rushdown()

#- Spells:
def Rushdown():
    d4Roll()

    spellDamage = (int(warrior_stats[3]) + diceVal)
    if int(warrior_stats[1]) >= 5:
        damage[0] = str(spellDamage)
        warrior_stats[1] = str(int(warrior_stats[1]) - 5)
        

def warrior_doing_stuff(stdscr):
    global warrior_attacking
    while warrior_attacking == True:
        stdscr.addstr(5, 21, "Warrior", curses.color_pair(3))
        if targets[0] == enemies[0]:
            stdscr.addstr(15,9, targets[0][7], curses.color_pair(2))

        elif targets[0] == enemies[1]:
            stdscr.addstr(15,52, targets[0][7], curses.color_pair(2))

        elif targets[0] == enemies[2]:
            stdscr.addstr(25,9, targets[0][7], curses.color_pair(2))

        elif targets[0] == enemies[3]:
            stdscr.addstr(25,52, targets[0][7], curses.color_pair(2))

        stdscr.refresh()
        wait(3)
        warrior_attacking = False
    stdscr.refresh()

#=========== Priest ===========
#- Attack choice:
def priest_attacks():

    if priest_selected_attack == 1:
        physicalAttack(priest_stats,targets[1])

    elif priest_selected_attack == 2:
        Exorcise()

    elif priest_selected_attack == 3:
        Mend()

#- Spells:
def Exorcise():
    d4Roll()

    spellDamage = (diceVal * 2)

    damage[1] = str(spellDamage)
    priest_stats[1] = str(int(priest_stats[1]) - 5)

def Mend():
    d6Roll()

    spellDamage = str(diceVal + int(priest_stats[3]))

    damage[1] = str(- int(spellDamage))
    priest_stats[1] = str(int(priest_stats[1]) - 3)

def priest_doing_stuff(stdscr):
    global priest_attacking
    while priest_attacking == True:
        if priest_selected_attack < 3:
            stdscr.addstr(5, 64, "Priest", curses.color_pair(3))
            if targets[1] == enemies[0]:
                stdscr.addstr(15,9, targets[1][7], curses.color_pair(2))

            elif targets[1] == enemies[1]:
                stdscr.addstr(15,52, targets[1][7], curses.color_pair(2))

            elif targets[1] == enemies[2]:
                stdscr.addstr(25,9, targets[1][7], curses.color_pair(2))

            elif targets[1] == enemies[3]:
                stdscr.addstr(25,52, targets[1][7], curses.color_pair(2))
        else:
            stdscr.addstr(5, 64, "Priest", curses.color_pair(3))
            if targets[1] == warrior_stats:
                stdscr.addstr(5,21, "Warrior", curses.color_pair(4))

            elif targets[1] == priest_stats:
                stdscr.addstr(5,64, "Priest", curses.color_pair(4))

        stdscr.refresh()
        wait(3)
        priest_attacking = False

    stdscr.refresh()

#========== Both ==========
#- Physical attack:
def physicalAttack(a, b):
    enemy = b
    Dmg = str(int(a[3]) - int(enemy[2]))

    if a[6] == "Warrior":
        damage[0] = Dmg
    else:
        damage[1] = Dmg

#=========== Enemies ===========
#- Enemie's stats lists:
menace_stats      = ['40' , '0', '0', '10', '10',"||             Menace             ||" ,"Menace"     ,"             Menace             ", "Menace                                                                              ||"]
Antonio           = ['99', '0', '0',  '0',  '0', "||             Antonio            ||" ,"Antonio"    ,"             Antonio            ", "Antonio                                                                             ||"]
orc_warrior_stats = ['30', '0', '5',  '2',  '2', "||           Orc Warrior          ||" ,"Orc Warrior","           Orc Warrior          ", "Orc Warrior                                                                         ||"]
orc_archer_stats  = ['10', '0', '3',  '4',  '5', "||           Orc Archer           ||" ,"Orc Archer" ,"           Orc Archer           ", "Orc Archer                                                                          ||"]
wolf_stats        = ['1' , '0', '0',  '5',  '7', "||              Wolf              ||" ,"Wolf"       ,"              Wolf              ", "Wolf                                                                                ||"]
#Index: 0 = Hp, 1 = Mp, 2 = Ap, 3 = Wp, 4 = Init, 5 = Card Name, 6 = Class name, 7 = Battle screen text, 8 = Menu text

#- Enemy types list
enemy_types       = [orc_warrior_stats, menace_stats, orc_archer_stats,wolf_stats]

#- Enemies functions:
def enemy_type():               #<-- selects the enemies
    global enemies
    global no_duplicates

    enemy_type_1st_roll = random.randrange(0,len(enemy_types))
    enemy_type_2nd_roll = random.randrange(0,len(enemy_types))
    enemy_type_3rd_roll = random.randrange(0,len(enemy_types))
    enemy_type_4th_roll = random.randrange(0,len(enemy_types))

    while enemy_type_2nd_roll == enemy_type_1st_roll:
        enemy_type_2nd_roll = random.randrange(0,len(enemy_types))
        enemy_type_3rd_roll = random.randrange(0,len(enemy_types))
        enemy_type_4th_roll = random.randrange(0,len(enemy_types))

    while enemy_type_3rd_roll == enemy_type_2nd_roll or enemy_type_3rd_roll == enemy_type_1st_roll:
        enemy_type_3rd_roll = random.randrange(0,len(enemy_types))
        enemy_type_4th_roll = random.randrange(0,len(enemy_types))

    while enemy_type_4th_roll == enemy_type_3rd_roll or enemy_type_4th_roll == enemy_type_2nd_roll or enemy_type_4th_roll == enemy_type_1st_roll:
        enemy_type_4th_roll = random.randrange(0,len(enemy_types))

    enemy_type_1 = enemy_types[enemy_type_1st_roll]
    enemy_type_2 = enemy_types[enemy_type_2nd_roll]
    enemy_type_3 = enemy_types[enemy_type_3rd_roll]
    enemy_type_4 = enemy_types[enemy_type_4th_roll]

    enemies = [enemy_type_1, enemy_type_2, enemy_type_3, enemy_type_4]

def check_duplicates(a,b,c,d):  #<-- checks for duplicate enemies, if it finds one it calls the enemy_type() function again
    if a == b:
        enemy_type(1)
    elif b == c or c == a:
        enemy_type(2)
    elif d == c or d == b or d == a:
        enemy_type(3)

def enemy_choose_target(a):     #<-- chooses the enemy target
    d4Roll()

    if diceVal % 2 == 0:
        targets[a + 2] = warrior_stats
    else:
        targets[a + 2] = priest_stats

def enemyPhysicalAttack(a,b):     #<-- calculates the damage of the enemy's physical attack
    global damage
    if b == "priest_dead":
        targets[a + 2] = warrior_stats
        target = targets[a + 2]
        dmg = str(int(enemies[a][3]) - int(target[2]))
        damage[a + 2] = dmg
    elif b == "warrior_dead":
        targets[a + 2] = priest_stats
        target = targets[a + 2]
        dmg = str(int(enemies[a][3]) - int(target[2]))
        damage[a + 2] = dmg
    else:
        target = targets[a + 2]
        dmg = str(int(enemies[a][3]) - int(target[2]))
        damage[a + 2] = dmg

def enemy_doing_stuff( stdscr):
    global enemy_1_attacking
    global enemy_2_attacking
    global enemy_3_attacking
    global enemy_4_attacking
    if enemy_1_attacking == True:
        if int(enemies[0][0]) > 0:
            while enemy_1_attacking == True:
                stdscr.addstr(15, 9, enemies[0][7], curses.color_pair(3))
                if targets[2] == warrior_stats:
                    stdscr.addstr(5, 21, "Warrior", curses.color_pair(2))
                elif targets[2] == priest_stats:
                    stdscr.addstr(5, 64, "Priest", curses.color_pair(2))
                stdscr.refresh()
                wait(3)
                enemy_1_attacking = False
        else:
            enemy_1_attacking = False

    if enemy_2_attacking == True:
        if int(enemies[1][0]) > 0:
            while enemy_2_attacking == True:
                stdscr.addstr(15, 52, enemies[1][7], curses.color_pair(3))
                if targets[3] == warrior_stats:
                    stdscr.addstr(5, 21, "Warrior", curses.color_pair(2))
                elif targets[3] == priest_stats:
                    stdscr.addstr(5, 64, "Priest", curses.color_pair(2))
                stdscr.refresh()
                wait(3)
                enemy_2_attacking = False
        else:
            enemy_2_attacking = False

    if enemy_3_attacking == True:
        if int(enemies[2][0]) > 0:
            while enemy_3_attacking == True:
                stdscr.addstr(25, 9, enemies[2][7], curses.color_pair(3))
                if targets[4] == warrior_stats:
                    stdscr.addstr(5, 21, "Warrior", curses.color_pair(2))
                elif targets[4] == priest_stats:
                    stdscr.addstr(5, 64, "Priest", curses.color_pair(2))
                stdscr.refresh()
                wait(3)
                enemy_3_attacking = False
        else:
            enemy_3_attacking = False

    if enemy_3_attacking == True:
        if int(enemies[2][0]) > 0:
            while enemy_4_attacking == True:        
                stdscr.addstr(25, 52, enemies[3][7], curses.color_pair(3))            
                if targets[5] == warrior_stats:
                    stdscr.addstr(5, 21, "Warrior", curses.color_pair(2))
                elif targets[5] == priest_stats:
                    stdscr.addstr(5, 64, "Priest", curses.color_pair(2))
                stdscr.refresh()
                wait(3)
                enemy_4_attacking = False
        else:
            enemy_4_attacking = False

    stdscr.refresh()

#=========== Stats Cards ===========
def make_ally_card(a,b,stdscr):                 #<-- Creates the cards that shows the stats of the allies
    CardBorders = "====================================" 
    Card1dgSpacinga = ["|| HP: " + str(a[0]) + "                          ||", "|| MP: " + str(a[1]) + "                          ||", "|| AP: " + str(a[2]) + "                          ||", "|| WP: " + str(a[3]) + "                          ||", "|| SPD: " + str(a[4]) + "                         ||"]
    Card2dgSpacinga = ["|| HP: " + str(a[0]) + "                         ||", "|| MP: " + str(a[1]) + "                         ||", "|| AP: " + str(a[2]) + "                         ||", "|| WP: " + str(a[3]) + "                         ||", "|| SPD: " + str(a[4]) + "                        ||"]
    Card1dgSpacingb = ["|| HP: " + str(b[0]) + "                          ||", "|| MP: " + str(b[1]) + "                          ||", "|| AP: " + str(b[2]) + "                          ||", "|| WP: " + str(b[3]) + "                          ||", "|| SPD: " + str(b[4]) + "                         ||"]
    Card2dgSpacingb = ["|| HP: " + str(b[0]) + "                         ||", "|| MP: " + str(b[1]) + "                         ||", "|| AP: " + str(b[2]) + "                         ||", "|| WP: " + str(b[3]) + "                         ||", "|| SPD: " + str(b[4]) + "                        ||"]
    
    if int(a[0]) > 0:
        index = 0
        stat = 0
        line = 7
        last = len(a) - 2
        stdscr.addstr(4,7, CardBorders)
        stdscr.addstr(5,7, a[5])
        stdscr.addstr(6,7, CardBorders)
        stdscr.addstr(4,50, CardBorders)
        stdscr.addstr(5,50, b[5])
        stdscr.addstr(6,50, CardBorders)
        while index < last:
            if len(str(a[stat])) == 1:
                stdscr.addstr(line, 7, Card1dgSpacinga[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(a[stat])) == 2:
                stdscr.addstr(line, 7, Card2dgSpacinga[stat])
                index += 1
                stat += 1
                line += 1
            stdscr.addstr(12,7, CardBorders)

    if int(b[0]) > 0:
        line = 7
        index = 0
        stat = 0
        while index < last:
            if len(str(b[stat])) == 1:
                stdscr.addstr(line, 50, Card1dgSpacingb[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(b[stat])) == 2:
                stdscr.addstr(line, 50, Card2dgSpacingb[stat])
                index += 1
                stat += 1
                line += 1
        stdscr.addstr(12,50, CardBorders)   

def make_enemy_card(a,b,c,d,stdscr):            #<-- Creates the cards that shows the stats of the enemies 
    CardBorders = "====================================" 
    Card1dgSpacinga = ["|| HP: " + str(a[0]) + "                          ||", "|| MP: " + str(a[1]) + "                          ||", "|| AP: " + str(a[2]) + "                          ||", "|| WP: " + str(a[3]) + "                          ||", "|| SPD: " + str(a[4]) + "                         ||"]
    Card2dgSpacinga = ["|| HP: " + str(a[0]) + "                         ||", "|| MP: " + str(a[1]) + "                         ||", "|| AP: " + str(a[2]) + "                         ||", "|| WP: " + str(a[3]) + "                         ||", "|| SPD: " + str(a[4]) + "                        ||"]
    Card1dgSpacingb = ["|| HP: " + str(b[0]) + "                          ||", "|| MP: " + str(b[1]) + "                          ||", "|| AP: " + str(b[2]) + "                          ||", "|| WP: " + str(b[3]) + "                          ||", "|| SPD: " + str(b[4]) + "                         ||"]
    Card2dgSpacingb = ["|| HP: " + str(b[0]) + "                         ||", "|| MP: " + str(b[1]) + "                         ||", "|| AP: " + str(b[2]) + "                         ||", "|| WP: " + str(b[3]) + "                         ||", "|| SPD: " + str(b[4]) + "                        ||"]
    Card1dgSpacingc = ["|| HP: " + str(c[0]) + "                          ||", "|| MP: " + str(c[1]) + "                          ||", "|| AP: " + str(c[2]) + "                          ||", "|| WP: " + str(c[3]) + "                          ||", "|| SPD: " + str(c[4]) + "                         ||"]
    Card2dgSpacingc = ["|| HP: " + str(c[0]) + "                         ||", "|| MP: " + str(c[1]) + "                         ||", "|| AP: " + str(c[2]) + "                         ||", "|| WP: " + str(c[3]) + "                         ||", "|| SPD: " + str(c[4]) + "                        ||"]
    Card1dgSpacingd = ["|| HP: " + str(d[0]) + "                          ||", "|| MP: " + str(d[1]) + "                          ||", "|| AP: " + str(d[2]) + "                          ||", "|| WP: " + str(d[3]) + "                          ||", "|| SPD: " + str(d[4]) + "                         ||"]
    Card2dgSpacingd = ["|| HP: " + str(d[0]) + "                         ||", "|| MP: " + str(d[1]) + "                         ||", "|| AP: " + str(d[2]) + "                         ||", "|| WP: " + str(d[3]) + "                         ||", "|| SPD: " + str(d[4]) + "                        ||"]

    if int(a[0]) > 0: 
        index = 0
        stat = 0
        line = 7
        last = len(a) - 4
        stdscr.addstr(4,7, CardBorders)
        stdscr.addstr(5,7, a[5])
        stdscr.addstr(6,7, CardBorders)
        while index < last:
            if len(str(a[stat])) == 1:
                stdscr.addstr(line, 7, Card1dgSpacinga[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(a[stat])) == 2:
                stdscr.addstr(line, 7, Card2dgSpacinga[stat])
                index += 1
                stat += 1
                line += 1
        stdscr.addstr(12,7, CardBorders)

    if int(b[0]) > 0:
        stdscr.addstr(4,50, CardBorders)
        stdscr.addstr(5,50, b[5])
        stdscr.addstr(6,50, CardBorders)
        last = len(a) - 4
        line = 7
        index = 0
        stat = 0
        while index < last:
            if len(str(b[stat])) == 1:
                stdscr.addstr(line, 50, Card1dgSpacingb[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(b[stat])) == 2:
                stdscr.addstr(line, 50, Card2dgSpacingb[stat])
                index += 1
                stat += 1
                line += 1
        stdscr.addstr(12,50, CardBorders)

    if int(c[0]) > 0:    
        index = 0
        stat = 0
        line = 17
        last = len(a) - 4
        stdscr.addstr(14,7, CardBorders)
        stdscr.addstr(15,7, c[5])
        stdscr.addstr(16,7, CardBorders)
        while index < last:
            if len(str(c[stat])) == 1:
                stdscr.addstr(line, 7, Card1dgSpacingc[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(c[stat])) == 2:
                stdscr.addstr(line, 7, Card2dgSpacingc[stat])
                index += 1
                stat += 1
                line += 1
            stdscr.addstr(22,7, CardBorders)

    if int(d[0]) > 0:
        stdscr.addstr(14,50, CardBorders)
        stdscr.addstr(15,50, d[5])
        stdscr.addstr(16,50, CardBorders)
        line = 17
        index = 0
        last = len(a) - 4
        stat = 0
        while index < last:
            if len(str(d[stat])) == 1:
                stdscr.addstr(line, 50, Card1dgSpacingd[stat])
                stat += 1
                index += 1
                line +=1
            elif len(str(d[stat])) == 2:
                stdscr.addstr(line, 50, Card2dgSpacingd[stat])
                index += 1
                stat += 1
                line += 1
        stdscr.addstr(22,50, CardBorders)

def draw_results_battle(a,b,c,d,e,f,stdscr):    #<-- Creates the cards that simultaneously shows the allie's stats and the enemie's stats
    global warrior_attacking

    CardBorders = "====================================" 
    Card1dgSpacinga = ["|| HP: " + str(a[0]) + "                          ||", "|| MP: " + str(a[1]) + "                          ||", "|| AP: " + str(a[2]) + "                          ||", "|| WP: " + str(a[3]) + "                          ||", "|| SPD: " + str(a[4]) + "                         ||"]
    Card2dgSpacinga = ["|| HP: " + str(a[0]) + "                         ||", "|| MP: " + str(a[1]) + "                         ||", "|| AP: " + str(a[2]) + "                         ||", "|| WP: " + str(a[3]) + "                         ||", "|| SPD: " + str(a[4]) + "                        ||"]
    Card1dgSpacingb = ["|| HP: " + str(b[0]) + "                          ||", "|| MP: " + str(b[1]) + "                          ||", "|| AP: " + str(b[2]) + "                          ||", "|| WP: " + str(b[3]) + "                          ||", "|| SPD: " + str(b[4]) + "                         ||"]
    Card2dgSpacingb = ["|| HP: " + str(b[0]) + "                         ||", "|| MP: " + str(b[1]) + "                         ||", "|| AP: " + str(b[2]) + "                         ||", "|| WP: " + str(b[3]) + "                         ||", "|| SPD: " + str(b[4]) + "                        ||"]
    Card1dgSpacingc = ["|| HP: " + str(c[0]) + "                          ||", "|| MP: " + str(c[1]) + "                          ||", "|| AP: " + str(c[2]) + "                          ||", "|| WP: " + str(c[3]) + "                          ||", "|| SPD: " + str(c[4]) + "                         ||"]
    Card2dgSpacingc = ["|| HP: " + str(c[0]) + "                         ||", "|| MP: " + str(c[1]) + "                         ||", "|| AP: " + str(c[2]) + "                         ||", "|| WP: " + str(c[3]) + "                         ||", "|| SPD: " + str(c[4]) + "                        ||"]
    Card1dgSpacingd = ["|| HP: " + str(d[0]) + "                          ||", "|| MP: " + str(d[1]) + "                          ||", "|| AP: " + str(d[2]) + "                          ||", "|| WP: " + str(d[3]) + "                          ||", "|| SPD: " + str(d[4]) + "                         ||"]
    Card2dgSpacingd = ["|| HP: " + str(d[0]) + "                         ||", "|| MP: " + str(d[1]) + "                         ||", "|| AP: " + str(d[2]) + "                         ||", "|| WP: " + str(d[3]) + "                         ||", "|| SPD: " + str(d[4]) + "                        ||"]
    Card1dgSpacinge = ["|| HP: " + str(e[0]) + "                          ||", "|| MP: " + str(e[1]) + "                          ||", "|| AP: " + str(e[2]) + "                          ||", "|| WP: " + str(e[3]) + "                          ||", "|| SPD: " + str(e[4]) + "                         ||"]
    Card2dgSpacinge = ["|| HP: " + str(e[0]) + "                         ||", "|| MP: " + str(e[1]) + "                         ||", "|| AP: " + str(e[2]) + "                         ||", "|| WP: " + str(e[3]) + "                         ||", "|| SPD: " + str(e[4]) + "                        ||"]
    Card1dgSpacingf = ["|| HP: " + str(f[0]) + "                          ||", "|| MP: " + str(f[1]) + "                          ||", "|| AP: " + str(f[2]) + "                          ||", "|| WP: " + str(f[3]) + "                          ||", "|| SPD: " + str(f[4]) + "                         ||"]
    Card2dgSpacingf = ["|| HP: " + str(f[0]) + "                         ||", "|| MP: " + str(f[1]) + "                         ||", "|| AP: " + str(f[2]) + "                         ||", "|| WP: " + str(f[3]) + "                         ||", "|| SPD: " + str(f[4]) + "                        ||"]

    if int(a[0]) > 0 or int(b[0]) > 0:
        if int(a[0]) > 0:
            stdscr.addstr(4,7, CardBorders)
            stdscr.addstr(5,7, a[5])
            stdscr.addstr(6,7, CardBorders)
            index = 0
            stat = 0
            line = 7
            last = len(a) - 2

            while index < last:
                if len(str(a[stat])) == 1:
                    stdscr.addstr(line, 7, Card1dgSpacinga[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(a[stat])) == 2:
                    stdscr.addstr(line, 7, Card2dgSpacinga[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(12,7, CardBorders)

        if int(b[0]) > 0:
            stdscr.addstr(4,50, CardBorders)
            stdscr.addstr(5,50, b[5])
            stdscr.addstr(6,50, CardBorders)
            index = 0
            stat = 0
            line = 7
            last = len(a) - 2

            while index < last:
                if len(str(b[stat])) == 1:
                    stdscr.addstr(line, 50, Card1dgSpacingb[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(b[stat])) == 2:
                    stdscr.addstr(line, 50, Card2dgSpacingb[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(12,50, CardBorders) 

        if int(c[0]) > 0:
            stdscr.addstr(14,7, CardBorders)
            stdscr.addstr(15,7, c[5])
            stdscr.addstr(16,7, CardBorders)
            index = 0
            stat = 0
            line = 17
            last = len(a) - 2

            while index < last:
                if len(str(c[stat])) == 1:
                    stdscr.addstr(line, 7, Card1dgSpacingc[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(c[stat])) == 2:
                    stdscr.addstr(line, 7, Card2dgSpacingc[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(22,7, CardBorders)

        if int(d[0]) > 0:
            stdscr.addstr(14,50, CardBorders)
            stdscr.addstr(15,50, d[5])
            stdscr.addstr(16,50, CardBorders)
            index = 0
            stat = 0
            line = 17
            last = len(a) - 2

            while index < last:
                if len(str(d[stat])) == 1:
                    stdscr.addstr(line, 50, Card1dgSpacingd[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(d[stat])) == 2:
                    stdscr.addstr(line, 50, Card2dgSpacingd[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(22,50, CardBorders) 

        if int(e[0]) > 0:
            stdscr.addstr(24,7, CardBorders)
            stdscr.addstr(25,7, e[5])
            stdscr.addstr(26,7, CardBorders)
            index = 0
            stat = 0
            line = 27
            last = len(a) - 2

            while index < last:
                if len(str(e[stat])) == 1:
                    stdscr.addstr(line, 7, Card1dgSpacinge[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(e[stat])) == 2:
                    stdscr.addstr(line, 7, Card2dgSpacinge[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(32,7, CardBorders)

        if int(f[0]) > 0:
            stdscr.addstr(24,50, CardBorders)
            stdscr.addstr(25,50, f[5])
            stdscr.addstr(26,50, CardBorders)
            index = 0
            stat = 0
            line = 27
            last = len(a) - 2

            while index < last:
                if len(str(f[stat])) == 1:
                    stdscr.addstr(line, 50, Card1dgSpacingf[stat])
                    stat += 1
                    index += 1
                    line +=1
                elif len(str(f[stat])) == 2:
                    stdscr.addstr(line, 50, Card2dgSpacingf[stat])
                    index += 1
                    stat += 1
                    line += 1
            stdscr.addstr(32,50, CardBorders)
            
        stdscr.refresh()

#============ Battle ============
#- Lists:
notarget   = ['0','0','0','0','0','0']
priorities = ['0','0','0','0','0','0']
damage     = ['0','0','0','0','0','0']
targets    = [notarget,notarget,priest_stats,warrior_stats,priest_stats,warrior_stats]
enemies    = [0,0,0,0,0,0]

#- Bool Variables:
attack            = True
warrior_attacking = False
priest_attacking  = False
enemy_1_attacking = False
enemy_2_attacking = False
enemy_3_attacking = False
enemy_4_attacking = False

#- Int Variables:
turn          = 0
selected_char = 0

#- Battle Phases Functions:
def init_phase(a,b,c,d,e,f):
    d20Roll()
    priorities[0] = str(diceVal + int(a[4])) 

    d20Roll()
    priorities[1] = str(diceVal + int(b[4]))

    d20Roll()
    priorities[2] = str(diceVal + int(c[4]))

    d20Roll()
    priorities[3] = str(diceVal + int(d[4]))

    d20Roll()
    priorities[4] = str(diceVal + int(e[4]))

    d20Roll()
    priorities[5] = str(diceVal + int(f[4]))

def action_phase(a,b,c,d,e,f,stdscr):
    global attack
    global warrior_attacking
    global priest_attacking
    global have_selected_moves
    global enemy_1_attacking
    global enemy_2_attacking
    global enemy_3_attacking
    global enemy_4_attacking

    enemy_choose_target(enemies.index(c))
    enemy_choose_target(enemies.index(d))
    enemy_choose_target(enemies.index(e))
    enemy_choose_target(enemies.index(f))

    init_phase(a,b,c,d,e,f)

    i = 100
   
    while i > 0:
        print_current_menu(stdscr, current_menu, current_row)
        
        if int(priorities[0]) == i and int(a[0]) > 0:
            warrior_attacks()
            targets[0][0] = str(int(targets[0][0]) - int(damage[0]))
            warrior_attacking = True

        if int(priorities[1]) == i and int(b[0]) > 0:
            priest_attacks() 
            targets[1][0] = str(int(targets[1][0]) - int(damage[1]))
            priest_attacking = True

        if int(priorities[2]) == i and int(c[0]) > 0:
            if int(targets[2][0]) <= 0 and targets[2] == warrior_stats:
                enemyPhysicalAttack(enemies.index(enemies[0]),"warrior_dead")
                targets[2][0] = str(int(targets[2][0]) - int(damage[2]))

            elif int(targets[2][0]) <= 0 and targets[2] == priest_stats:
                enemyPhysicalAttack(enemies.index(enemies[0]), "priest_dead")
                warrior_stats[0] = str(int(warrior_stats[0]) - int(damage[2]))
            else:
                enemyPhysicalAttack(enemies.index(enemies[0]), "party_alive")
                targets[2][0] = str(int(targets[2][0]) - int(damage[2]))
            enemy_1_attacking = True

        if int(priorities[3]) == i and int(d[0]) > 0:
            if int(targets[3][0]) <= 0 and targets[3] == warrior_stats:
                enemyPhysicalAttack(enemies.index(enemies[1]),"warrior_dead")
                targets[3][0] = str(int(targets[3][0]) - int(damage[3]))
            elif int(targets[3][0]) <= 0 and targets[3] == priest_stats:
                enemyPhysicalAttack(enemies.index(enemies[1]), "priest_dead")
                warrior_stats[0] = str(int(warrior_stats[0]) - int(damage[3]))
            else:
                enemyPhysicalAttack(enemies.index(enemies[1]), "party_alive")
                targets[3][0] = str(int(targets[3][0]) - int(damage[3]))
            enemy_2_attacking = True

        if int(priorities[4]) == i and int(e[0]) > 0:
            if int(targets[4][0]) <= 0 and targets[4] == warrior_stats:
                enemyPhysicalAttack(enemies.index(enemies[2]),"warrior_dead")
                targets[4][0] = str(int(targets[4][0]) - int(damage[3]))
            elif int(targets[4][0]) <= 0 and targets[4] == priest_stats:
                enemyPhysicalAttack(enemies.index(enemies[2]), "priest_dead")
                warrior_stats[0] = str(int(warrior_stats[0]) - int(damage[4]))
            else:
                enemyPhysicalAttack(enemies.index(enemies[2]), "party_alive")
                targets[4][0] = str(int(targets[4][0]) - int(damage[4]))
            enemy_3_attacking = True

        if int(priorities[5]) == i and int(f[0]) > 0:
            if int(targets[5][0]) <= 0 and targets[5] == warrior_stats:
                enemyPhysicalAttack(enemies.index(enemies[3]),"warrior_dead")
                targets[5][0] = str(int(targets[5][0]) - int(damage[5]))
            elif int(targets[5][0]) <= 0 and targets[5] == priest_stats:
                enemyPhysicalAttack(enemies.index(enemies[3]), "priest_dead")
                warrior_stats[0] = str(int(warrior_stats[0]) - int(damage[5]))
            else:
                enemyPhysicalAttack(enemies.index(enemies[3]), "party_alive")
                targets[5][0] = str(int(targets[5][0]) - int(damage[5]))
            enemy_4_attacking = True
        
        i -= 1
        
    reset_variables()

#=========== Menus ===========
#- Lists:
menu_0_opts  = []
menu_1_opt   = ['opt_1']
menu_2_opts  = ['opt_1','Exit']
menu_3_opts  = ['opt_1', 'opt_2', 'Exit']
menu_4_opts  = ['opt_1', 'opt_2', 'opt_3', 'Exit']
menu_5_opts  = ['opt_1', 'opt_2', 'opt_3', 'opt_4', 'Exit']

#- Int variables:
current_row = 0
current_menu = 9
have_selected_moves = 0

#- Bool variables:
checking_allies = False
no_duplicates = False

#- Functions:
def battle_main(stdscr):
    global current_menu
    global current_row
    global menu
    global attack

    enemy_type()

    curses.curs_set(0)                                          #<-- turn off cursor blinking

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) #<-- color scheme for selected row
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    


    battle_menu(stdscr, current_row)                            #<-- print the main battle menu

    while 1:
        if int(enemies[0][0]) <= 0 and int(enemies[1][0]) <= 0 and int(enemies[2][0]) <= 0 and int(enemies[3][0]) <= 0:
            current_menu = 10
        if int(priest_stats[0]) <= 0 and int(warrior_stats[0]) <= 0:
            current_menu = 10
        if int(warrior_stats[0]) > 0 and int(priest_stats[0]) > 0:
            if targets[0] != notarget and targets[1] != notarget:
                current_menu = 7
                print_current_menu(stdscr, current_menu, current_row)
                while attack == True:
                    action_phase(warrior_stats, priest_stats, enemies[0], enemies[1], enemies[2], enemies[3],stdscr)
        elif int(warrior_stats[0]) > 0 and int(priest_stats[0]) <= 0:
            if targets[0] != notarget:

                current_menu = 7
                print_current_menu(stdscr, current_menu, current_row)
                while attack == True:
                    action_phase(warrior_stats, priest_stats, enemies[0], enemies[1], enemies[2], enemies[3],stdscr)
        elif int(warrior_stats[0]) <= 0 and int(priest_stats[0]) > 0:
            if targets[1] != notarget:

                current_menu = 7
                print_current_menu(stdscr, current_menu, current_row)
                while attack == True:
                    action_phase(warrior_stats, priest_stats, enemies[0], enemies[1], enemies[2], enemies[3],stdscr)
                
            
        
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            make_choice(current_menu, current_row)

        print_current_menu(stdscr, current_menu, current_row)

def battle_menu(stdscr, selected_row_idx):
    global menu
    menu = menu_2_opts
    stdscr.clear()
    stdscr.addstr(0,0,
        """=============================================================================================
||                                    The battle begins                                    ||
=============================================================================================
||                                                                                         ||
||     Fight                                                                               ||
||                                                                                         ||
||     Check stats                                                                         ||
||                                                                                         ||
=============================================================================================""")
    if selected_row_idx == 0:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, 4, "-->Fight")
        stdscr.attroff(curses.color_pair(1))
    elif selected_row_idx == 1:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(6, 4, "-->Check stats")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def char_select_menu(stdscr, selected_row_idx):
    global menu
    global menu_idx
    global targets
    stdscr.clear()
    stdscr.addstr(0,0,"""=============================================================================================
||                                Select the character                                     ||
=============================================================================================""")
    if have_selected_moves == 1 or int(warrior_stats[0]) <= 0 and int(priest_stats[0]) > 0:
        menu = menu_2_opts
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Priest                                                                              ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Priest")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(6, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()

    elif have_selected_moves ==  2 or int(priest_stats[0]) <= 0 and int(warrior_stats[0]) > 0:
        menu = menu_2_opts
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Warrior                                                                             ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Warrior")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(6, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        
    elif have_selected_moves ==  0:
        menu = menu_3_opts
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Warrior                                                                             ||
||                                                                                         ||
||     Priest                                                                              ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Warrior")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(6, 4, "-->Priest")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 2:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(8, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()

def attacks_menu(stdscr, selected_row_idx):
    global menu
    menu = menu_3_opts
    stdscr.clear()
    stdscr.addstr(0,0,"""=============================================================================================
||                                       Attacks                                           ||
=============================================================================================
||                                                                                         ||
||     Physical                                                                            ||
||                                                                                         ||
||     Spells                                                                              ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
    if selected_row_idx == 0:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, 4, "-->Physical")
        stdscr.attroff(curses.color_pair(1))
    elif selected_row_idx == 1:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(6, 4, "-->Spells")
        stdscr.attroff(curses.color_pair(1))
    elif selected_row_idx == 2:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(8, 4, "-->Exit")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def spells_menu(stdscr, selected_row_idx):
    global menu
    stdscr.clear()
    if selected_char == 1:
        menu = menu_2_opts
        mana = warrior_stats[1]
        stdscr.addstr(0,0,"=============================================================================================\n||                                       SPELLS                            Current Mana: " + str(mana) + " ||\n=============================================================================================")
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Rushdown:                                                                           ||
||     - Uses magic to enhance their speed and maximize impact damage.      (costs 5 mana) ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Rushdown:")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(7, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
    elif selected_char == 2:
        menu = menu_3_opts
        stdscr.clear()
        mana = priest_stats[1]
        if int(mana) < 10:
            stdscr.addstr(0,0,"=============================================================================================\n||                                       SPELLS                            Current Mana: " + str(mana) + " ||\n=============================================================================================")
        else:
            stdscr.addstr(0,0,"=============================================================================================\n||                                       SPELLS                           Current Mana: " + str(mana) + " ||\n=============================================================================================")
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Exorcism:                                                                           ||
||      - THE POWER OF CHRIST COMPELLS YOU!!!                               (costs 5 mana) ||
||                                                                                         ||
||     Mend:                                                                               ||
||      - Heals the target                                                  (costs 3 mana) ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Exorcism:")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(7, 4, "-->Mend:")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 2:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(10, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()

def not_enough_mana(stdscr):
    global current_menu
    if selected_char == 1:
        mana = warrior_stats[1]
        stdscr.addstr(0,0,"=============================================================================================\n||                                   NOT ENOUGH MANA                       Current Mana: " + str(mana) + " ||\n=============================================================================================")
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Rushdown:                                                                           ||
||     - Uses magic to enhance their speed and maximize impact damage.      (costs 5 mana) ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        stdscr.refresh()
        wait(1)
        current_menu = 4

    if selected_char == 2:
        stdscr.clear()
        mana = priest_stats[1]
        if int(mana) < 10:
            stdscr.addstr(0,0,"=============================================================================================\n||                                   NOT ENOUGH MANA                       Current Mana: " + str(mana) + " ||\n=============================================================================================")
        else:
            stdscr.addstr(0,0,"=============================================================================================\n||                                   NOT ENOUGH MANA                      Current Mana: " + str(mana) + " ||\n=============================================================================================")
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Exorcism:                                                                           ||
||      - THE POWER OF CHRIST COMPELLS YOU!!!                               (costs 5 mana) ||
||                                                                                         ||
||     Mend:                                                                               ||
||      - Heals the target                                                  (costs 3 mana) ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        stdscr.refresh()
        wait(1)
        current_menu = 4
        stdscr.refresh()

def target_select_menu(stdscr, selected_row_idx):
    global menu
    stdscr.clear()
    stdscr.addstr(0,0,"""=============================================================================================
||                                 Select the target                                       ||
=============================================================================================""")
    if selected_char == 2 and priest_selected_attack == 3 and int(warrior_stats[0]) > 0:
        menu = menu_3_opts
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Warrior                                                                             ||
||                                                                                         ||
||     Priest                                                                              ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(4, 4, "-->Warrior")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(6, 4, "-->Priest")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 2:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(8, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
    elif selected_char == 2 and priest_selected_attack == 3 and int(warrior_stats[0]) < 0:
        menu = menu_2_opts
        stdscr.addstr(3,0,"""||                                                                                         ||
||     Priest                                                                              ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(6, 4, "-->Priest")
            stdscr.attroff(curses.color_pair(1))
        elif selected_row_idx == 1:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(8, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
    else:
        menu = menu_5_opts
        enemy1 = enemies[0]
        enemy2 = enemies[1]
        enemy3 = enemies[2]
        enemy4 = enemies[3]
        stdscr.addstr(3,0,"||                                                                                         ||")
        stdscr.addstr(4,0,"||     " + enemy1[8] + "\n||                                                                                         ||")
        stdscr.addstr(6,0,"||     " + enemy2[8] + "\n||                                                                                         ||")
        stdscr.addstr(8,0,"||     " + enemy3[8] + "\n||                                                                                         ||")
        stdscr.addstr(10,0,"||     " + enemy4[8])
        stdscr.addstr(11,0,"""||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
        if selected_row_idx == 0:
            if int(enemies[0][0]) > 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(4, 4, "-->" + enemy1[6])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(4, 4, "-->" + enemy1[6])
                stdscr.attroff(curses.color_pair(2))
        elif selected_row_idx == 1:
            if int(enemies[1][0]) > 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(6, 4, "-->" + enemy2[6])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(6, 4, "-->" + enemy2[6])
                stdscr.attroff(curses.color_pair(2))
        elif selected_row_idx == 2:
            if int(enemies[2][0]) > 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(8, 4, "-->" + enemy3[6])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(8, 4, "-->" + enemy3[6])
                stdscr.attroff(curses.color_pair(2))
        elif selected_row_idx == 3:
            if int(enemies[3][0]) > 0:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(10, 4, "-->" + enemy4[6])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(10, 4, "-->" + enemy4[6])
                stdscr.attroff(curses.color_pair(2))
        elif selected_row_idx == 4:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(12, 4, "-->Exit")
            stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()

def action_phase_results(stdscr):
    global menu
    menu = menu_0_opts
    stdscr.clear()
    stdscr.addstr(0,0,"""=============================================================================================
||                                        Battling                                         ||
=============================================================================================
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
=============================================================================================
""")
    draw_results_battle(warrior_stats, priest_stats, enemies[0], enemies[1], enemies[2], enemies[3], stdscr)
    warrior_doing_stuff(stdscr)
    priest_doing_stuff(stdscr)
    enemy_doing_stuff(stdscr)
    stdscr.refresh()

def select_stats_menu(stdscr, selected_row_idx):
    global menu
    menu = menu_3_opts
    stdscr.clear()
    stdscr.addstr(0,0,
        """=============================================================================================
||                                       Check Stats                                       ||
=============================================================================================
||                                                                                         ||
||     Allies                                                                              ||
||                                                                                         ||
||     Enemies                                                                             ||
||                                                                                         ||
||     Exit                                                                                ||
||                                                                                         ||
=============================================================================================""")
    if selected_row_idx == 0:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, 4, "-->Allies")
        stdscr.attroff(curses.color_pair(1))
    elif selected_row_idx == 1:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(6, 4, "-->Enemies")
        stdscr.attroff(curses.color_pair(1))
    elif selected_row_idx == 2:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(8, 4, "-->Exit")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def stats_menu(stdscr):
    global menu
    menu = menu_1_opt
    if checking_allies == True:
        stdscr.clear()
        stdscr.addstr(0,0,"""=============================================================================================
||                                          Allies                                         ||
=============================================================================================
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
=============================================================================================
""")
        make_ally_card(warrior_stats, priest_stats, stdscr)
        stdscr.refresh()
    else:
        stdscr.addstr(0,0,"""=============================================================================================
||                                         Enemies                                         ||
=============================================================================================
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
||                                                                                         ||
=============================================================================================""")
        make_enemy_card( enemies[0], enemies[1],enemies[2], enemies[3],stdscr)

def make_choice(a, b):
    global checking_allies
    global current_menu
    global current_row
    global selected_char
    global warrior_selected_attack
    global priest_selected_attack
    global menu
    global have_selected_moves
    global attack

    if a == 0: #battle start menu
        if targets[0] != notarget and targets[1] != notarget:
            targets[0] = notarget
            targets[1] = notarget
        if b == 0:
            current_row = 0
            current_menu = 1
        elif b == 1:
            current_row = 0
            current_menu = 2

    elif a == 1: #character selection menu
        if have_selected_moves == 0:
            menu = menu_3_opts
            if b == 0:
                selected_char = 1

                current_row = 0
                current_menu = 3

            elif b == 1:
                selected_char = 2

                current_row = 0
                current_menu = 3

            elif b == 2:
                selected_char = 0
                current_row = 0
                current_menu = 0

        if have_selected_moves == 1 or int(warrior_stats[0]) <= 0 and int(priest_stats[0]) > 0:
            menu = menu_2_opts
            if b == 0:
                selected_char = 2
                current_row = 0
                current_menu = 3
            elif b == 1:
                current_row = 0
                current_menu = 0
                selected_char = 0

        if have_selected_moves == 2 or int(priest_stats[0]) <= 0 and int(warrior_stats[0]) > 0:
            if b == 0:
                selected_char = 1
                current_row = 0
                current_menu = 3
            elif b == 1:
                current_row = 0
                current_menu = 0
                selected_char = 0

    elif a == 2: #stats Menu
        menu = menu_3_opts
        if b == 0:
            checking_allies = True
            current_row = 0
            current_menu = 6
        if b == 1:
            checking_allies = False
            current_row = 0
            current_menu = 6
        if b == 2:
            current_row = 1
            current_menu = 0

    elif a == 3: #attacks Menu
        menu = menu_3_opts
        if b == 0:
            if selected_char == 1:
                warrior_selected_attack = 1
            elif selected_char == 2:
                priest_selected_attack = 1
            current_row = 0
            current_menu = 5
        elif b == 1:
            current_row = 0
            current_menu = 4
        elif b == 2:
            current_row = 0
            current_menu = 1
            selected_char = 0

    elif a == 4: #Spells Menu
        if selected_char == 1:
            menu = menu_2_opts
            if b == 0:
                if int(warrior_stats[1]) >= 5:
                    warrior_selected_attack = 2
                    current_row = 0
                    current_menu = 5
                else:
                    current_menu = 8
            elif b == 1:
                current_row = 0
                current_menu = 3
        elif selected_char == 2:
            menu = menu_3_opts
            if b == 0:
                priest_selected_attack = 2
                if int(priest_stats[1]) >= 5:
                    priest_selected_attack = 2
                    current_row = 0
                    current_menu = 5
                else:
                    priest_selected_attack = 0
                    current_menu = 8
            elif b == 1:
                priest_selected_attack = 3
                if int(priest_stats[1]) >= 3:
                    priest_selected_attack = 3
                    current_row = 0
                    current_menu = 5
                else:
                    priest_selected_attack = 0
                    current_menu = 8
            elif b == 2:
                current_row = 0
                current_menu = 3

    elif a == 5: #Target Menu
        if priest_selected_attack == 3 and selected_char == 2:
            menu = menu_3_opts

            if b == 0:
                targets[1] = warrior_stats
                current_row = 0
                current_menu = 0
                have_selected_moves = 2

            elif b == 1:
                targets[1] = priest_stats
                current_row = 0
                current_menu = 0
                have_selected_moves = 2

            elif b == 4:
                current_row = 0
                current_menu = 3
                priest_selected_attack = 0 

        else:
            menu = menu_5_opts

            if b == 0:
                if int(enemies[0][0]) > 0:
                    if selected_char == 1:
                        targets[0] = enemies[0]
                        have_selected_moves = 1
                        current_row = 0
                        current_menu = 0
                    elif selected_char == 2:
                        targets[1] = enemies[0]
                        have_selected_moves = 2
                        current_row = 0
                        current_menu = 0
                else:
                    current_row = 0
                    current_menu = 5

            elif b == 1:
                if int(enemies[1][0]) > 0:
                    if selected_char == 1:
                        targets[0] = enemies[1]
                        have_selected_moves = 1
                        current_row = 0
                        current_menu = 0
                    elif selected_char == 2:
                        targets[1] = enemies[1]
                        have_selected_moves = 2
                        current_row = 0
                        current_menu = 0
                else:
                    current_row = 1
                    current_menu = 5

            elif b == 2:
                if int(enemies[2][0]) > 0:
                    if selected_char == 1:
                        targets[0] = enemies[2]
                        have_selected_moves = 1
                        current_row = 0
                        current_menu = 0
                    elif selected_char == 2:
                        targets[1] = enemies[2]
                        have_selected_moves = 2
                        current_row = 0
                        current_menu = 0
                else:
                    current_row = 2
                    current_menu = 5

            elif b == 3:
                if int(enemies[3][0]) > 0:
                    if selected_char == 1:
                        targets[0] = enemies[3]
                        have_selected_moves = 1
                        current_row = 0
                        current_menu = 0
                    elif selected_char == 2:
                        targets[1] = enemies[3]
                        have_selected_moves = 2
                        current_row = 0
                        current_menu = 0
                else:
                    current_row = 0
                    current_menu = 3

            elif b == 4:
                current_row = 0
                current_menu = 3
                if selected_char == 1:
                    warrior_selected_attack = 0
                elif selected_char == 2:
                    priest_selected_attack = 0

    elif a == 6: #Checking stats Menu
        menu = menu_1_opt
        if b == 0:
            current_row = 0
            current_menu = 2
    elif a == 9:
        if b == 0:
            current_row = 0
            current_menu = 0
    
    elif a == 10:
        menu = menu_1_opt
        if b == 0:
            quit()

def print_current_menu(stdscr, current_menu, current_row):  
    global attack  
    if current_menu == 0:
        battle_menu(stdscr, current_row)
    elif current_menu == 1:
        char_select_menu(stdscr, current_row)
    elif current_menu == 2:
        select_stats_menu(stdscr, current_row)
    elif current_menu == 3:
        attacks_menu(stdscr, current_row)
    elif current_menu == 4:
        spells_menu(stdscr, current_row)
    elif current_menu == 5:
        target_select_menu(stdscr, current_row)
    elif current_menu == 6:
        stats_menu(stdscr)
    elif current_menu == 7:
        attack = True
        action_phase_results(stdscr)
    elif current_menu == 8:
        not_enough_mana(stdscr)
    elif current_menu == 9:
        start_screen(stdscr,current_row)
    elif current_menu == 10:
        end_screen(stdscr, current_row)

def end_screen(stdscr,selected_row_idx):
    global current_menu
    current_menu = 10
    if int(enemies[0][0]) <= 0 and int(enemies[1][0]) <= 0 and int(enemies[2][0]) <= 0 and int(enemies[3][0]) <= 0:
        stdscr.addstr(0,0,
        """=============================================================================================
||                                      YOU WIN!                                           ||
=============================================================================================
||                                                                                         ||
||                                        Exit                                             ||
||                                                                                         ||
=============================================================================================""")
    elif int(priest_stats[0]) <= 0 and int(warrior_stats[0]) <= 0:
        stdscr.addstr(0,0,
        """=============================================================================================
||                                      YOU LOSE!                                          ||
=============================================================================================
||                                                                                         ||
||                                        Exit                                             ||
||                                                                                         ||
=============================================================================================""")
    if selected_row_idx == 0:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, 40, "-->Exit")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

def start_screen(stdscr,selected_row_idx):
    global menu
    menu = menu_1_opt
    stdscr.clear()
    stdscr.addstr(0,0,"""=============================================================================================
||                                    Text Battles                                         ||
=============================================================================================
||                                                                                         ||
||                                       BEGIN!                                            ||
||                                                                                         ||
=============================================================================================""")
    if selected_row_idx == 0:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(4, 41, "-->BEGIN!")
        stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

#=========== Reset ===========
def reset_variables():
    global enemy_1_attacking
    global enemy_2_attacking
    global enemy_3_attacking
    global enemy_4_attacking
    global warrior_selected_attack
    global priest_selected_attack
    global priorities
    global damage
    global targets
    global warrior_attacking
    global priest_attacking
    global selected_char
    global menu_idx
    global current_row
    global current_menu
    global have_selected_moves
    global attack
    global checking_allies
    global diceVal
    global turn

    warrior_selected_attack = 0
    priest_selected_attack = 0
    priorities = ['0','0','0','0','0','0']
    damage     = ['0','0','0','0','0','0']
    targets    = [notarget,notarget,priest_stats,warrior_stats,priest_stats,warrior_stats]
    warrior_attacking = False
    priest_attacking  = False
    enemy_1_attacking = False
    enemy_2_attacking = False
    enemy_3_attacking = False
    enemy_4_attacking = False
    selected_char = 0
    menu_idx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    current_row = 0
    current_menu = 0
    have_selected_moves = 0
    attack = False
    checking_allies = False
    diceVal = 0

    turn += 1

def reset_all():
    global menu
    global enemy_1_attacking
    global enemy_2_attacking
    global enemy_3_attacking
    global enemy_4_attacking
    global warrior_selected_attack
    global priest_selected_attack
    global priorities
    global damage
    global targets
    global warrior_attacking
    global priest_attacking
    global selected_char
    global menu_idx
    global current_row
    global current_menu
    global have_selected_moves
    global attack
    global checking_allies
    global diceVal
    global turn
    global no_duplicates
    global enemies
    global enemy_types
    global warrior_stats
    global priest_stats
    global menace_stats
    global orc_warrior_stats
    global orc_archer_stats
    global wolf_stats
    global enemy_types

    warrior_selected_attack = 0
    priest_selected_attack = 0
    priorities = ['0','0','0','0','0','0']
    damage     = ['0','0','0','0','0','0']
    targets    = [notarget,notarget,priest_stats,warrior_stats,priest_stats,warrior_stats]
    warrior_attacking = False
    priest_attacking  = False
    enemy_1_attacking = False
    enemy_2_attacking = False
    enemy_3_attacking = False
    enemy_4_attacking = False
    selected_char = 0
    menu_idx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    current_row = 0
    current_menu = 9
    have_selected_moves = 0
    attack = False
    checking_allies = False
    diceVal = 0
    turn = 0
    warrior_stats = ['35',  '5', '2', '5', '2', "||            Warrior             ||", "Warrior"]
    priest_stats  = ['20', '25', '0', '2', '6', "||            Priest              ||", "Priest" ]
    no_duplicates = False
    enemies    = [0,0,0,0,0,0]
    menace_stats      = ['10' , '0', '0', '6', '10', "||             Menace             ||" ,"Menace"     ,"             Menace             ", "Menace                                                                              ||"]
    orc_warrior_stats = ['15', '0', '2',  '2',  '2', "||           Orc Warrior          ||" ,"Orc Warrior","           Orc Warrior          ", "Orc Warrior                                                                         ||"]
    orc_archer_stats  = ['10', '0', '2',  '4',  '5', "||           Orc Archer           ||" ,"Orc Archer" ,"           Orc Archer           ", "Orc Archer                                                                          ||"]
    wolf_stats        = ['5' , '0', '0',  '5',  '7', "||              Wolf              ||" ,"Wolf"       ,"              Wolf              ", "Wolf                                                                                ||"]
    enemy_types       = [orc_warrior_stats, menace_stats, orc_archer_stats,wolf_stats]

reset_all()
curses.wrapper(battle_main)