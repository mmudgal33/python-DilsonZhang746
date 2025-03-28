codes = []
for value in range(1,1264):
    
    codes.append(str(value)+'.py')
    
print(codes)




# import OS module
import os

# This is my path
path = "D://finacusjobhackathon//CodingVideos//campusX python DSA//python DilsonZhang746//leetcode-master//solutions//codes"

# to store files in a list
list1 = []

# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.py' in f:
            # print(f)
            list1.append(f)
            

print(list1)



list2=[]
for i in list1[:-1]:
    # print(i)
    i = i.replace('.py', '')
    list2.append(i)
    
print(list2)


list2=[int(x) for x in list2]


list2.sort()
list2=[str(x) for x in list2]

print(list2[2])

print(list2)

list3=[]
for i in list2[:-1]:
    # print(i)
    i = i+'.py'
    list3.append(i)
    
print(list3)
            

# lines_list = ["First line", "Second line", "Third line"]
# with open(file_path, 'w') as f:
#     text = "\n".join(lines_list)
#     f.write(text)




for i in list3:
    with open(i,'r') as file:
    # with open(str(i)+'.py','r') as file:
        # file = open('code.py','r')
        data = file.read()
        file.close()
        # f = open('code.py','w')
        f = open('code.py','a')
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write(str(i) + " " + data)
        f.close()
        
        
        

    
        
        
        
        
fr=open('1.py','r')
f = open('code.py','w')
f.write(fr)
f.close()