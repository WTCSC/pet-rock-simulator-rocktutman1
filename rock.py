import os, time, random
print ("Welcome to the pet rock simulator, Please run in a large terminal for the best expierence")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

Strength = 3
Endurance = 3
Technique = 0
Toughness = 3
Fatigue = 0
Hunger = 5
Happiness = 5
playing = 1
turns = 10
t = 0
junk = ""
Name = input ("What would you like to name your rock? ")
for num in range(20):
    t += 1
    if t == 1: junk = "⟊⧈⧵⋇⧭⩧⊱⟠⧖⩓⩂⧞⋉⧄⊰⧦⋎⫬⩀⩶⧊⧳⟘⫟⋴⧺⩲⧮⊼⟢"
    if t == 2: junk = "⋕⟛⫤⩳⧡⟍⧱⩵⊟⧘⟗⧀⋒⫠⩎⟞⧔⩠⋔⟢⧥⊹⫣⧇⋎⟙⧚⩛⫨⟤"
    if t == 3: junk = "⫷⧓⩱⋍⧂⟊⩑⧆⫲⊭⟜⧡⩖⧙⋕⩌⧻⧯⟟⫗⩀⧌⫦⧱⋑⩚⧿⊼⧞⟤"
    if t == 4: 
        junk = "⟡⧉⟧⧢⫒⋇⟣⩆⫧⟜⧿⩉⋊⧌⧥⫨⟠⊹⩟⧎⧀⟚⫕⩯⧵⋴⫛⟧⧛"
        t = 0
    print(f"\rRandomizing Personality {junk}", end="")
    time.sleep(.2)
print ("")
personality = random.randint(1,4)
if personality == 1: print ("Your rock's personality is lazy \n +50%s fatigue gained from all sources \n +50% fatigue recovered from resting \n +2 fatigue recovered from eating")
if personality == 2: print ("Your rock's personality is toxic \n Loose 5 hapiness when loosing a battle \n Gain 5 hapiness when winning a battle \n Gain 1 hapiness when at least one stat is above 7")
if personality == 3: print ("Your rock's personality is manic \n Fatigue is always at 0/10 \n +100% hunger gain")
if personality == 4: print ("Your rock's personality is reserved \n -2 to Strength and Technique, \n +2 to Endurance and Toughness")
input ("Enter to continue")
while playing == 1:
    if personality == 3:
        Fatigue = 0
    if turns > 0:
        print (f"=== Your pet rock {Name} ===")
        if personality == 4:
            print (f"Strength: {Strength-2}/10 -- {Strength}/10 before reserved")
            print (f"Endurance: {Endurance+2}/10 -- {Endurance}/10 before reserved")
            print (f"Technique: {Technique-2}/10 -- {Technique}/10 before reserved")
            print (f"Toughness: {Toughness+2}/10 -- {Toughness}/10 before reserved")
        else:
            print (f"Strength: {Strength}/10")
            print (f"Endurance: {Endurance}/10")
            print (f"Technique: {Technique}/10")
            print (f"Toughness: {Toughness}/10")
        print (f"Fatigue: {Fatigue}/10")
        print (f"Hunger: {Hunger}/10")
        print (f"Happiness: {Happiness}/10")
        input ("Enter to continue")
        action = input ("How would you like to train {name}? \n 1. Weightlifting \n 2. Running \n 3. Sparring \n 4. Eat \n 5. Lay on the couch \n")
        if action == "1": pass
        elif action == "2": pass
        elif action == "3": pass
        elif action == "4": pass
        elif action == "5": pass
    if turns == 0:
        print ("Battle day")
        exit()
    turns -= 1
    clear()