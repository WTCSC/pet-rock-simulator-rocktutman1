import time, random, curses
print ("Welcome to the pet rock simulator, Please run in a large terminal for the best expierence")

def clear():
    print ("\n" * 100)
def Weightlifting(stdscr):
    count = 0
    block = "█"
    space = " "
    direction = "R"
    gabagool = 0
    failure = False
    stdscr.nodelay(True)
    print("Hit any key to reverse bar direction, try to use as few reverses as possible")
    time.sleep(5)
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
    print ("Training finished")
    input ("Enter to continue")
    return correct
Strength = 3
Endurance = 3
Technique = 0
Toughness = 3
Fatigue = 0
Hunger = 5
Happiness = 5
playing = 1
turns = 7
t = 0
junk = ""
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
    time.sleep(.2)
print ("")
personality = random.randint(1,4)
if personality == 1: print (f"{name}'s personality is lazy \n +50% fatigue gained from all sources \n +50% fatigue recovered from resting \n +2 fatigue recovered from eating")
if personality == 2: print (f"{name}'s personality is toxic \n Loose 5 hapiness when loosing a battle \n Gain 5 hapiness when winning a battle \n Gain 1 hapiness when at least one stat is above 7")
if personality == 3: print (f"{name}'s personality is rude \n Strength +4 \n -1 hapiness at start of turn")
if personality == 4: print (f"{name}'s personality is reserved \n -2 to Strength and Technique, \n +2 to Endurance and Toughness")
input ("Enter to continue")

# While loop you never leave begins here
while playing == 1: 
    print ("while loop running (debug)")
    if turns > 0:
        print (f"=== Your pet rock {name} ===")
        if personality == 4:
            print (f"Strength: {Strength-2}/10 -- {Strength}/10 before reserved")
            print (f"Endurance: {Endurance+2}/10 -- {Endurance}/10 before reserved")
            print (f"Technique: {Technique-2}/10 -- {Technique}/10 before reserved")
            print (f"Toughness: {Toughness+2}/10 -- {Toughness}/10 before reserved")
        else:
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
        input ("Enter to continue")
        print (f"How would you like to train {name}? \n 1. Weightlifting \n 2. Running \n 3. Sparring \n 4. Eat \n 5. Lay on the couch \n")
        action = input ("Enter 1-5")
        if action == "1": 
            gabagool = curses.wrapper(Weightlifting) #I stole this curses stuff from google
            Hunger += 2
            print (gabagool, "debug")
            if gabagool == False:
                Endurance += 1
                Fatigue += 4
                Happiness -= 3
                Strength += .5
                print ("You gained \n 1 Endurance \n 4 Fatigue \n -3 Happiness \n .5 Strength \n 2 Hunger")
            else:
                if gabagool == 9:
                    print ("Perfect score!")
                    print (f"You gained \n {10-Strength} Strength \n 2 Hunger \n 5 Technique")
                    Strength = 10
                    Technique += 5
                elif gabagool == 10:
                    Strength += 2
                    Fatigue += 1.5
                    print (f"You gained \n 2 Strength \n 2 Hunger \n 1.5 Fatigue")
                else:
                    Strength += 1.5
                    Fatigue += 2
                    print (f"You gained \n 1.5 Strength \n 2 Hunger \n 2 Fatigue")
        elif action == "2": 
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
            print (f"You gained \n {correct * .25} Endurance \n {round(correct * .1,1)} Technique and Toughness \n {.5 * (7-correct)} Fatigue")
            if correct > 5:
                print (" 1.5 Hunger\n 1 Happiness")
            else:
                print (" 1 Hunger\n -1 Happiness")
        elif action == "3": pass
        elif action == "4": pass
        elif action == "5": pass
    if turns == 0:
        print ("Battle day")
        exit()
    input("Enter to continue")
    turns -= 1
    clear()
