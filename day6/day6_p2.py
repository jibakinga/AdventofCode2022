with open("day6.txt") as f:
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    index = 0
    current = 0
    for line in f:
        for x in line:

            if index==14:
                for b in range(1,len(a)):
                    a[b-1]=a[b]
                index = 13
            if index<14:
                a[index] = x
                current+=1
                index+=1
            if len(set(a))==len(a) and 0 not in a:
                print(current)
                break