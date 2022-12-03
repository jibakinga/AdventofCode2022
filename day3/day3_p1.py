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

for line in f:
    if line[-1]=="\n":
        line=line[:-1]
    list1=line[:int(len(line)/2)]
    list2=line[int(len(line)/2):]
    
    for element in set(list1):
        if element in set(list2):
            sum_priorities+=priorities[element]
            
print(sum_priorities)       
    