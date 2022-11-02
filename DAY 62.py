#DAY 62
f = open("story.txt","r")
data = f.read().split()
print('#'.join(data))
f.close()

'''
#or 
f = open("story.txt","r")
data = f.read().split()
for word in data:
    print(word,end='#')
f.close()

#or to do line wise
f = open("story.txt","r")
data = f.readlines()
for line in data:
    print("#".join(line.split()))
f.close()

#another way for above code 
f = open("story.txt","r")
data = f.readlines()
for line in data:
    for word in line.split():
        print(word,end'#')
    print()
f.close()
    
'''