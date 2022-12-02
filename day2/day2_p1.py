f = open("day2.txt", "r")
sign_dict = {"X":1,
             "Y":2,
             "Z":3}

opp_a = {"X":3,
         "Y":6,
         "Z":0}

opp_b = {"X":0,
         "Y":3,
         "Z":6}

opp_c = {"X":6,
         "Y":0,
         "Z":3}

total = 0
for line in f:
    opponent,you=line.split(" ")
    you=you[0]
    total+=sign_dict[you]
    
    if opponent=="A":
        total+=opp_a[you]
    elif opponent=="B":
        total+=opp_b[you]
    elif opponent=="C":
        total+=opp_c[you]

    
        
print(total)    
    
