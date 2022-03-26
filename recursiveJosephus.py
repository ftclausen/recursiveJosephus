#!/usr/bin/env python3
#
# Friedrich "Fred" Clausen study notes
#
# A recursive implementation of the Josephus problem.  Seems to work but the
# programmatic recursion is not quite like the mathetical recurrence.  Notes
# inline. See my blog post at
#
# https://ftclausen.github.io/mathematics/josephus-problem-revisited/
# 
# Which is based on the topic in Concrete Mathematics (Graham, Knuth, Patashnik)
import sys

def josephus(people):
    if people <= 1:
        print(f'DEBUG: Base case, people == {people}, hit; returning')
        return 1
    # Recur on even
    if people % 2 == 0:
        print(f'DEBUG: Even person count: {people}')
        # The math recurrence is J(2n) = 2J(n) - 1
        # Here we are using division to go to the next recurrence.
        # In the math there is no division in the recurrence.
        return 2 * josephus(people / 2) - 1
    # Recur on odd
    else:
        print(f'DEBUG: Odd person count: {people}')
        # The match recurrence is J(2n + 1) = 2J(n) + 1 As with even we are
        # using division _and_ making the numer even so we can divide since you
        # can't have "half a person".  In the math these steps don't happen
        return 2 * josephus((people - 1) / 2) + 1 

if len(sys.argv) == 2:
    safe_spot = josephus(int(sys.argv[1]))
    print(f'Safe spot is: {safe_spot}')
else:
    print(f'Usage: {sys.argv[0]} <people in circle>')

