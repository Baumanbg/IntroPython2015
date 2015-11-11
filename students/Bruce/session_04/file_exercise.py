#initialize list and dictionary
temp_list = []
lang_dict = {}

f = open('students.txt')
line = f.readline()
while True:
    line = f.readline()
    if not line:
        break
    count = 0
    for i in line:
        if i == ":":
            temp_list = line[count+1:-1].split()
            for x in temp_list:
                if x in lang_dict:
                    n = lang_dict[x]
                    lang_dict[x]= n + 1
                else:
                    lang_dict[x]= 1
        count +=1
f.close()
all_keys = list(lang_dict.keys()) 
for i in range(len(all_keys)):
    print(" %s, #students: %i"%(all_keys[i],lang_dict[all_keys[i]]))  