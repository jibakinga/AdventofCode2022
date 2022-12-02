f = open("day2.txt", "r")

opp_a = {"X":3+0,
         "Y":1+3,
         "Z":2+6}

opp_b = {"X":1+0,
         "Y":2+3,
         "Z":3+6}

opp_c = {"X":2+0,
         "Y":3+3,
         "Z":1+6}

total = 0
for line in f:
    opponent,you=line.split(" ")
    you=you[0]
    
    if opponent=="A":
        total+=opp_a[you]
    elif opponent=="B":
        total+=opp_b[you]
    elif opponent=="C":
        total+=opp_c[you]

    
        
print(total)    
    
