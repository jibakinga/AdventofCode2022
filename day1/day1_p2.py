f = open("day1.txt", "r")

elf_num=1
curr_sum=0
max_sum1=0
max_sum2=0
max_sum3=0

for line in f:
    if len(line)==1:
        
        print(max_sum1,max_sum2,max_sum3)
        if curr_sum>max_sum3:
            if curr_sum>max_sum2:
                if curr_sum>max_sum1:
                    max_sum3=max_sum2
                    max_sum2=max_sum1
                    max_sum1=curr_sum
                else:
                    max_sum3=max_sum2
                    max_sum2=curr_sum
            else:
                max_sum3=curr_sum
            
        elf_num+=1
        curr_sum=0
    else:
        curr_sum+=int(line.strip())



if curr_sum>max_sum3:
    if curr_sum>max_sum2:
        if curr_sum>max_sum1:
            max_sum3=max_sum2
            max_sum2=max_sum1
            max_sum1=curr_sum
        else:
            max_sum3=max_sum2
            max_sum2=curr_sum
    else:
        max_sum3=curr_sum





print(max_sum1+max_sum2+max_sum3)
