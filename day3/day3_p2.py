f = open(r"C:\Users\Minahil\Desktop\adv\day3\day3.txt", "r")

priorities={};

key=ord("a")
for i in range(26):
    priorities[chr(key)]=i+1
    key+=1

key=ord("A")
for i in range(26):
    priorities[chr(key)]=i+1+26
    key+=1

sum_priorities=0
count=0
l_arr=[]

for line in f:
    if line[-1]=="\n":
        line=line[:-1]
    
    l_arr.append(line)
    count+=1;
    
    if count==3:
        for element in set(l_arr[0]):
            if element in set(l_arr[1]) and element in set(l_arr[2]):
                sum_priorities+=priorities[element]    
    
        count=0
        l_arr=[]
        
print(sum_priorities)       
    