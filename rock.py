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
personality = random.randit(1,4)
if personality == 1: print ("Your rock's personality is lazy")
if personality == 2: print ("Your rock's personality is toxic")
if personality == 3: print ("Your rock's personality is manic")
if personality == 4: print ("Your rock's personality is reserved")
input ("Enter to continue")
while playing == 1:

    if turns > 0:
        print (f"=== Your pet rock {Name} ===")
        print (f"Strength: {Strength}/10")
        print (f"Endurance: {Endurance}/10")
        print (f"Technique: {Technique}/10")
        print (f"Toughness: {Toughness}/10")
        print (f"Fatigue: {Fatigue}/10")
        print (f"Hunger: {Hunger}/10")
        print (f"Happiness: {Happiness}/10")
        action = input ("What would you like to do? \n 1. Weightlifting \n 2. Running \n 3. Sparring \n 4. Eat \n 5. Lay on the couch")
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