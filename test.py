import time, random
print ("Welcome to the pet rock simulator, Please run in a large terminal for the best expierence")

def clear():
    print ("\n" * 100)
def Weightlifting():
    count = 0
    block = "█"
    space = " "
    direction = "R"
    print("Hit enter to stop the bar \nDont let it overflow")
    for i in range(300):
        if count == 30:
            direction = "L"
        if direction == "R":
            count += 1
        elif direction == "L":
            count -= 1
        print (f"[{block*count}{space*(30-count)}]")
        time.sleep(.2)
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
        action = input (f"How would you like to train {name}? \n 1. Weightlifting \n 2. Running \n 3. Sparring \n 4. Eat \n 5. Lay on the couch \n")
        if action == "1": 
            Weightlifting()
        elif action == "2": 
            correct = Running()
            Endurance += correct * .25
            Happiness += 1
            Technique = round(Technique + (correct * .1), 1)
            Toughness = round(Toughness + (correct * .1), 1)
            Fatigue += .5 * (7-correct)
            Hunger += 1
            if correct > 5:
                Hunger += .5
            print (f"You gained \n {correct * .25} Endurance \n 1 Happiness \n {round(correct * .1,1)} Technique and Toughness \n {.5 * (7-correct)} Fatigue")
            if correct > 5:
                print (" 1.5 Hunger")
            else:
                print (" 1 Hunger")
        elif action == "3": pass
        elif action == "4": pass
        elif action == "5": pass
    if turns == 0:
        print ("Battle day")
        exit()
    input("Enter to continue")
    turns -= 1
    clear()
