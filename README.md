# lunch
This is a shitty python script with piss poor fundamental logic that all it does is picks where to eat lunch based on a few conditions.  At this time you can specify two parameters- josh and (cheap or ncheap).  

Conditions are:

Argument 1 (optional): josh 

Argument 2: cheap or ncheap

If you do not use the josh parameter, it will just look for cheap or ncheap options being passed.

Usage:
The script loads choices from two lists, cheapeats.txt and notcheapeats.txt.  It then randomly chooses a place from this list, as long as it hasn't been chosen in the past 5 choices.  The past 5 picks are stored in the notagain.txt file.  The places josh will never let us go are stored in vetolist.txt

[SCENARIO 1: Josh is coming and we have to eat somewhere cheap]
>python lunch.py josh cheap

This will pick a lunch spot from the cheapeats.txt list, and removes the restaurants found in the vetolist.txt file.

[SCENARIO 2: Josh is not coming, and we don't care what the cost is]
>python lunch.py

This will simply merge the cheap and notcheap lists, and randomly choose from the list as long as its not in the last 5 places chosen.

[SCENARIO 3: Josh is coming, but we don't care about the cost]
>python lunch.py josh

Picks from both cheap places and not cheap places, but removes the ones Josh doesn't like.

[SCENARIO 4: Josh is coming, and we wanna be fancy]
>python lunch.py josh ncheap

Picks from not cheap place list, removes places Josh doesn't like.
