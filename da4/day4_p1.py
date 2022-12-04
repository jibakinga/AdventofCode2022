with open("day4.txt","r") as file:

    count = 0

    for line in file:
        if line[-1]=="\n":
            line=line[:-1]
                
        a,b = line.split(",")
        a1,a2 = a.split("-")
        b1,b2 = b.split("-")
             
        if int(a1)>=int(b1) and int(a2)<=int(b2):
            count+=1
        elif int(b1)>=int(a1) and int(b2)<=int(a2):
            count+=1         

    print(count)