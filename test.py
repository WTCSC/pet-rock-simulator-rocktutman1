import time

for i in range(10):
    print(f"\rProcessing: {i+1}/10", end="")
    time.sleep(0.5)
print("\nDone!") # Print a final newline after the loop