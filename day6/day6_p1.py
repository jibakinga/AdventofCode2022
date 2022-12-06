with open("day6.txt") as f:
    a = [0,0,0,0]
    index = 0
    current = 0
    for line in f:
        for x in line:

            if index==4:
                a[0]=a[1]
                a[1]=a[2]
                a[2]=a[3]
                index = 3
            if index<4:
                a[index] = x
                current+=1
                index+=1
            if len(set(a))==len(a) and 0 not in a:
                print(current)
                break