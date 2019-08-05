
for a in range(0,2):
    for b in range(0, 2):
        for c in range(0, 2):
            # !(A || B) || ( (A || C) && !(B || !C) )
            if not (a or b) or ( (a or c) and not (b or not c) ):
                result = 1
            else:
                result = 0
            print(f"{a}  |  {b}  |  {c}  = {result}")