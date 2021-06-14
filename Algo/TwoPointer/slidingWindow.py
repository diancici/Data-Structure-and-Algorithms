## Framework
from collections import defaultdict
def slideWindow(s, t):
    need = defaultdict(int)
    window = defaultdict(int)

    for c in t:
        need[c] += 1

    left = 0
    right = 0
    start = 0
    valid = 0

    # Moveforward the right pointer until reach the end: enlarge the window
    while (right < len(s)):
        c = s[right]
        right += 1
        # update data in window 
        # ...

        # debug: print(left, right)

        # Move forward left pointer if meet the requirement: shrink the window
        while(valid == len(need.keys())):
            d = s[left]
            d += 1
            # update data in window




        
