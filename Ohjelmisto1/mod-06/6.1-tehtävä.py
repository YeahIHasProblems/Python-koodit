import random

def nopanheitto():
    return random.randint(1,6)
    
while True:
    onkokuusi = nopanheitto()
    print(onkokuusi)
    if onkokuusi == 6:
        break
