import time, random, curses

def clear():
    print ("\n" * 100)
clear()
print ("Welcome to the rock boxing simulator, Please run in a large terminal for the best expierence")
def Weightlifting(stdscr):
    count = 0
    block = "█"
    space = " "
    direction = "R"
    gabagool = 0
    failure = False
    stdscr.nodelay(True)
    print("Hit any key to reverse bar direction, try to use as few reverses as possible")
    time.sleep(2.5)
    for i in range(300):
        key = stdscr.getch()
        if key != -1:
            gabagool += 1 
            if direction == "R":
                direction = "L"
            elif direction == "L":
                direction = "R"
        if count == -1 or count == 31:
            failure = True
            break
        if direction == "R":
            count += 1
        elif direction == "L":
            count -= 1
        print (f"\r[{block*count}{space*(30-count)}]", end="")
        if (i < 100):
            time.sleep(.1)
        elif (i < 200):
            time.sleep(.07)
        else:
            time.sleep(.04)
    if failure == True:
        print (f"\r You overtrained, Holy fatigue maxing. You bounced the bar {gabagool} times")
        time.sleep(5)
        return False
    else:
        print (f"You bounced the bar {gabagool} times")
        time.sleep(5)
        return gabagool
def Running():
    correct = 0
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for i in range(7):
        clear()
        target = random.choice(letters)
        print ("Get ready for a skill check")
        time.sleep(1)
        print (f"Hit {target} within 1.5 seconds!")
        start = time.time()
        KeyHit = input ("")
        if KeyHit == target and time.time() - start < 1.5:
            print ("Correct")
            correct += 1
        elif time.time() - start > 1.5 and KeyHit != target:
            print ("You took too long to hit the wrong key")
        elif time.time() - start > 1.5:
            print (f"You took too long! ({time.time() - start} seconds)")
        elif KeyHit != target:
            print ("Wrong key!")
        time.sleep(1)
    print (f"Training finished ----- {correct}/7 correct")
    input ("Enter to continue")
    clear()
    return correct
def Sparring(Name):
    print (f"Pick the right counter to teach {Name}!")
    endc = 0
    tech = 0
    for i in range(5):
        loops = random.randint(9,12)
        for num in range(loops):
            if num == 0 or num == 4 or num == 8:
                print (f"\r{Name} Will use Jab", end = "")
            if num == 1 or num == 5 or num == 9:
                print (f"\r{Name} Will use Spinning Backfist", end = "")
            if num == 2 or num == 6 or num == 10:
                print (f"\r{Name} Will use Crotch Punch", end = "")
            if num == 3 or num == 7 or num == 11:
                print (f"\r{Name} Will use Sweep", end = "")
            time.sleep(.3)
            print ("\r                                                                                  " , end = "")
        if loops == 9:
            print (f"\r{Name} will use Jab")
            print ("How do you respond? \n 1. Raise Guard \n 2. Duck \n 3. Hook redirect \n 4. Wide hook")
            move = input ("Enter 1-4: ")
            if move == "1":
                print (f"You block the jab, {Name} gains .5 technique")
                tech += .5
            elif move == "2":
                print ("You get clipped")
            elif move == "3":
                print (f"You counter the jab, {Name} gains .5 toughness")
                endc += .5
            elif move == "4":
                print ("The Wide hook is too slow!")
            else:
                print ("Invalid input, you get hit")
        if loops == 10:
            print (f"\r{Name} will use Spinning Backfist")
            print ("How do you respond? \n 1. Wide hook \n 2. Lean back \n 3. Block Straight \n 4. Inside jab")
            move = input ("Enter 1-4: ")
            if move == "1":
                print ("The Wide hook is too Slow!")
            elif move == "2":
                print (f"You dodge the backfist, {Name} gains .5 technique")
                tech += .5
            elif move == "3":
                print ("The backfist goes around your block!")
            elif move == "4":
                print (f"You intercept the backfist, {Name} gains .5 toughness")
                endc += .5
            else:
                print ("Invalid input, you get hit")
        if loops == 11:
            print (f"\r{Name} will use Crotch Punch")
            print ("How do you respond? \n 1. Knee to the head \n 2. Jab \n 3. Step back \n 4. Guard high")
            move = input ("Enter 1-4: ")
            if move == "1":
                print (f"You interrupt the crotch punch, {Name} gains .5 toughness")
                endc += .5
            elif move == "2":
                print (f"{Name} ducks the jab!")
            elif move == "3":
                print (f"You dodge the crotch punch, {Name} gains .5 technique")
                tech += .5
            elif move == "4":
                print ("The crotchpunch goes under your guard!")
            else:
                print ("Invalid input, you get hit")
        if loops == 12:
            print (f"\r{Name} will use Sweep")
            print ("How do you respond? \n 1. Gaurd high \n 2. Knee to the head \n 3. Jab \n 4. Jump")
            move = input ("Enter 1-4: ")
            if move == "1":
                print ("The sweep goes under your guard!")
            elif move == "2":
                print (f"You interrupt the sweep, {Name} gains .5 toughness")
                endc += .5
            elif move == "3":
                print (f"{Name} ducks the jab!")
            elif move == "4":
                print (f"You dodge the sweep, {Name} gains .5 technique")
                tech += .5
            else:
                print ("Invalid input, you get hit")
        time.sleep(2)
        clear()
    print ("Sparring complete")
    return endc, tech
Strength = 3
Endurance = 3
Technique = 0
Toughness = 3
Fatigue = 0
Hunger = 3
Happiness = 5
playing = 1
turns = 7
t = 0
danger = 0
hapdanger = 0
junk = ""
NotFirst = False
name = input ("What would you like to name your rock? ")
for num in range(20):
    t += 1
    if t == 1: junk = "⟊⧈⧵⋇⧭⩧⊱⟠⧖⩓⩂⧞⋉⧄⊰⧦⋎⫬⩀⩶⧊⧳⟘⫟⋴⧺⩲⧮⊼⟢"
    if t == 2: junk = "⋕⟛⫤⩳⧡⟍⧱⩵⊟⧘⟗⧀⋒⫠⩎⟞⧔⩠⋔⟢⧥⊹⫣⧇⋎⟙⧚⩛⫨⟤"
    if t == 3: junk = "⫷⧓⩱⋍⧂⟊⩑⧆⫲⊭⟜⧡⩖⧙⋕⩌⧻⧯⟟⫗⩀⧌⫦⧱⋑⩚⧿⊼⧞⟤"
    if t == 4: 
        junk = "⟡⧉⟧⧢⫒⋇⟣⩆⫧⟜⧿⩉⋊⧌⧥⫨⟠⊹⩟⧎⧀⟚⫕⩯⧵⋴⫛⟧⧛"
        t = 0
    print(f"\rRandomizing {name}'s Personality {junk}", end="")
    time.sleep(.1)
print ("")
personality = random.randint(1,4)
if personality == 1: print (f"{name}'s personality is lazy \n +50% fatigue gained from all sources \n +50% fatigue recovered from resting \n +3 fatigue recovered from eating")
if personality == 2: print (f"{name}'s personality is toxic \n Gain 1 happiness when at least one stat is above 7 \n 20% chance to gain a random stat at start of turn")
if personality == 3: print (f"{name}'s personality is rude \n Strength +4 \n -1 hunger at start of turn")
if personality == 4: print (f"{name}'s personality is reserved \n -2 to Strength and Technique, \n +2 to Endurance and Toughness")
input ("Enter to continue")
clear()
# While loop you never leave begins here
while playing == 1: 
    if personality == 3:#rude hunger loss
        Hunger += 1
        print ("-1 Hunger from rude personality")
    if personality == 2:#toxic stat gain
        if Strength > 7 or Technique > 7 or Endurance > 7 or Toughness > 7:
            Happiness += 1
            print ("+1 Happiness from toxic personality")
        statgain = random.randint(1,5)
        if statgain == 1:
            statgain = random.randint(1,4)
            if statgain == 1:
                Strength += 1
                print ("+1 Strength from toxic personality")
            if statgain == 2:
                Endurance += 1
                print ("+1 Endurance from toxic personality")
            if statgain == 3:
                Technique += 1
                print ("+1 Technique from toxic personality")
            if statgain == 4:
                Toughness += 1
                print ("+1 Toughness from toxic personality")
    if turns > 0:
        if NotFirst == True:#personality info
            if personality == 1: print (f"{name}'s personality is lazy \n +50% fatigue gained from all sources \n +50% fatigue recovered from resting \n +3 fatigue recovered from eating")
            if personality == 2: print (f"{name}'s personality is toxic \n Gain 1 happiness when at least one stat is above 7 \n 20% chance to gain a random stat at start of turn")
            if personality == 3: print (f"{name}'s personality is rude \n Strength +4 \n -1 hunger at start of turn")
            if personality == 4: print (f"{name}'s personality is reserved \n -2 to Strength and Technique, \n +2 to Endurance and Toughness")
        print (f"=== Your pet rock {name} ===")
        if personality == 4:#print reserved stats
            print (f"Strength: {Strength-2}/10 -- {Strength}/10 before reserved")
            print (f"Endurance: {Endurance+2}/10 -- {Endurance}/10 before reserved")
            print (f"Technique: {Technique-2}/10 -- {Technique}/10 before reserved")
            print (f"Toughness: {Toughness+2}/10 -- {Toughness}/10 before reserved")
        else: #print normal stats
            if personality == 3:
                print (f"Strength {Strength+4}/10 -- {Strength}/10 before rude")
            else:
                print (f"Strength: {Strength}/10")
            print (f"Endurance: {Endurance}/10")
            print (f"Technique: {Technique}/10")
            print (f"Toughness: {Toughness}/10")
        print (f"Fatigue: {Fatigue}/10")
        print (f"Hunger: {Hunger}/10")
        print (f"Happiness: {Happiness}/10")
        if danger == 1:#game overs
            if Hunger > 10:
                print (f"{name} is too hungry to continue training, game over")
                exit()
            if Fatigue > 10:
                print (f"{name} is too tired to continue training, game over")
                exit()
        if hapdanger == 1: #game overs pt2
            if Happiness < 0:
                print (f"{name} is too unhappy to continue training, game over")
                exit()
        if True == True: #handles danger warning I just wanted to decluter
            if Hunger > 10 and Fatigue > 10:
                danger = 1
                print (f"! ! ! Warning, {name} is very hungry and tired ! ! !")
            elif Hunger > 10:
                danger = 1
                print (f"! ! ! Warning, {name} is very hungry ! ! !")
            elif Fatigue > 10:
                danger = 1
                print (f"! ! ! Warning, {name} is very tired ! ! !")
            if Happiness < 0:
                hapdanger = 1
                print (f"! ! ! Warning, {name} is very unhappy ! ! !")
        input ("Enter to continue")
        clear()
        print (f"How would you like to train {name}? \n 1. Weightlifting \n 2. Running \n 3. Sparring \n 4. Eat \n 5. Lay on the couch \n 6. View stats \n 7. quit")
        action = input ("Enter 1-6: ")
        if action == "1": #Weighlifting
            gabagool = curses.wrapper(Weightlifting) #I stole this curses stuff from google
            clear()
            Hunger += 2
            if gabagool == False:
                Endurance += 1
                Fatigue += 4
                Happiness -= 3
                Strength += .5
                print ("You gained \n 1 Endurance \n 4 Fatigue \n -3 Happiness \n .5 Strength \n 2 Hunger")
                if personality == 1:
                    Fatigue += 2
                    print (" 2 Fatigue from lazy personality")
            else:
                if gabagool == 9:
                    print ("Perfect score!")
                    print (f"You gained \n {10-Strength} Strength \n 2 Hunger \n 5 Technique")
                    Strength = 10
                    Technique += 5
                elif gabagool == 10:
                    Strength += 2
                    Fatigue += 1.5
                    Hunger -= .5
                    print (f"You gained \n 2 Strength \n 1.5 Hunger \n 1 Fatigue")
                    if personality == 1:
                        Fatigue += .75
                        print (" .75 Fatigue from lazy personality")
                elif gabagool == 11:
                    Strength += 1.5
                    Fatigue += 1.5
                    print (f"You gained \n 1.5 Strength \n 2 Hunger \n 1.5 Fatigue")
                    if personality == 1:
                        Fatigue += .75
                        print (" .75 Fatigue from lazy personality")
                else:
                    Strength += 1.5
                    Hunger += 2
                    Fatigue += 2
                    print (f"You gained \n 1.5 Strength \n 2 Hunger \n 2 Fatigue")
                    if personality == 1:
                        Fatigue += 1
                        print (" 1 Fatigue from lazy personality")
        elif action == "2": #running
            clear()
            correct = Running()
            Endurance += correct * .25
            Technique = round(Technique + (correct * .1), 1)
            Toughness = round(Toughness + (correct * .1), 1)
            Fatigue += .5 * (7-correct)
            Hunger += 1
            if correct > 5:
                Hunger += .5
                Happiness += 1
            else:
                Happiness -= 1
            if personality == 1:
                Fatigue += .25 * (7-correct)
                print (f" {.25 * (7-correct)} Fatigue from lazy personality")
            print (f"You gained \n {correct * .25} Endurance \n {round(correct * .1,1)} Technique and Toughness \n {.5 * (7-correct)} Fatigue")
            if correct > 5:
                print (" 1.5 Hunger\n 1 Happiness")
            else:
                print (" 1 Hunger\n -1 Happiness")
        elif action == "3": #sparring
            clear()
            endc, tech = Sparring(name)
            Toughness += endc
            Technique += tech
            Fatigue += 1
            Hunger += 1
            Happiness -= 1
            print (f"You gained \n {endc} Toughness \n {tech} Technique \n 1 Fatigue \n 1 Hunger \n -1 Happiness")
            if personality == 1:
                Fatigue += .5
                print (" .5 Fatigue from lazy personality")
        elif action == "4": #eat
            if personality == 1:
                Fatigue -= 3
                print ("-3 Fatigue from lazy personality")
            if Hunger > 10:
                Hunger = 5
                print (f"{name} Was very Hungry, Hunger set to 5")
            else:
                Hunger -= 4
                print (f"{name} Wasn't very Hungry, Hunger reduced by 4")
        elif action == "5": #rest
            if Fatigue > 10:
                if personality == 1:
                    Fatigue = 3
                    print (f"{name} Was very tired and lazy, Fatigue set to 3")
                else:
                    Fatigue = 5
                    print (f"{name} Was very tired, Fatigue set to 5")
            else:
                if personality == 1:
                    Fatigue -= 6
                    print (f"{name} Wasn't very tired, Fatigue reduced by 6")
                else:
                    Fatigue -= 4
                    print (f"{name} Wasn't very tired, Fatigue reduced by 4")
            Happiness += 2
            print ("Happiness increased by 2")
        elif action == "6": #view stats
            clear()
            NotFirst = True
            danger = 0
            hapdanger = 0
            continue
        elif action == "7": #quit
            print ("byebye")
            exit()
        else: # other options 
            print (f"Thats not a option! {name} is upset and looses 1 happiness")
            Happiness -= 1
    input("Enter to continue")
    NotFirst = True
    clear()
    if Strength > 10:
        Strength = 10
    if Endurance > 10:
        Endurance = 10
    if Technique > 10:
        Technique = 10
    if Toughness > 10:
        Toughness = 10
    if Fatigue < 0:
        Fatigue = 0
    if Hunger < 0:
        Hunger = 0
    if Hunger < 10:
        danger = 0
    if Fatigue < 10:
        danger = 0
