with open("day5.txt") as f:
    stack = []
    lines = []
    for line in f:
        if len(line)>1:
            if line[0]in["["," "] and line[1]!="1":     
                    lines.append(line)
            
            if line[1]=="1":
                for i in range(0,int(line[-3])):
                    stack.append([])
                for x in lines:
                    index = 1
                    i=0
                    while index<len(x):
                        if x[index]!=" ":
                            stack[i].append(x[index])
                        index+=4
                        i+=1
        
            if line[0]=="m":
                line = line.split(" ")
                for i in range(0,int(line[1])):
                    from_stack = int(line[3])-1
                    to_stack = int(line[5])-1
                    stack[to_stack].insert(0,stack[from_stack][0])
                    stack[from_stack] = stack[from_stack][1:]
for line in stack:
    print(line[0],end="")
        