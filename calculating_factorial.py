# Simple countdown timer using sleep().

import time

seconds = 5
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")
