'''
name="ajay new ajay"
word="ay"
count=0
i=0
end=len(word)
while i<len(name):
    if name[i:end] == word:
         print("found at",i)
         count=count+1
    i=i+1
    end=end+1
        
else:
    print(count)


name = 'sunday monday tuesday'
key = 'day'
count = 0
start = 0 
end = len(key)
while start<len(name)-1:                                                                           
    if name[start:end] == key:
        print("found at", start)
        count+=1
    start+=1
    end+=1
else:
    print(count)



name='ajay deril and akil'
word='a'
count=0
i=0
end=len(word)
while i<len(name):
    if name[i:end]==word:
        count=count+1
    i=i+1
    end=end+1
else:
    print(count)
'''
row = 1
while row<=9:
    col = 1
    while col<=9:
        print("*",end=' ')
        col+=1
    print()
    row+=1
