import time
import random

def quick_time_event(target_key, time_limit):
    print(f"Press '{target_key}' within {time_limit} seconds!")
    start_time = time.time()
    
    try:
        user_input = input("Your input: ")
        end_time = time.time()
        reaction_time = end_time - start_time

        if user_input.lower() == target_key.lower() and reaction_time <= time_limit:
            print(f"Success! You reacted in {reaction_time:.2f} seconds.")
            return True
        else:
            print(f"Failed! You either pressed the wrong key or were too slow ({reaction_time:.2f}s).")
            return False
    except EOFError: # Handles potential issues with input in some environments
        print("Input interrupted. Failed!")
        return False

if __name__ == "__main__":
    keys = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
    target_key = random.choice(keys)
    time_limit = 1.5

    print("Get ready for a Quick Time Event!")
    time.sleep(1) # Short delay before starting

    if quick_time_event(target_key, time_limit):
        print("You won the minigame!")
    else:
        print("You lost the minigame!")