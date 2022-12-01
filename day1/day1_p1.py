f = open("day1.txt", "r")

elf_num=1
curr_sum=0
max_sum=0

for line in f:
    if len(line)==1:
        if curr_sum>max_sum:
            max_sum=curr_sum
            
        elf_num+=1
        curr_sum=0
    else:
        curr_sum+=int(line.strip())

print(max_sum)
