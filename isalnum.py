####################################################  function
def isalnum(pincode):
    for letter in pincode:
        if letter>='0' and letter<='9' or (letter>='a' and letter<='z') or (letter>='A' and letter<='Z'):
            continue
        else:
            print(False)
            break
    else:
        print(True)


pincode = "Chennai600042"
isalnum(pincode)






########################################for loop
name="ajay***** 1234"
for letter in name:
    if letter>='0' and letter<='9' or (letter>='a' and letter<='z') :
        continue
    else:
        print(False)
        break
else:
    print(True)
        
       
 


####################################              While loop
name="123*"
i=0
while i<len(name):
    if name[i]>='0' and name[i]<='9' or name[i]>='a' and name[i]<='z':
        i+=1
        
                                                                                                 ###  dobut
    else:
        print(False)
        break
        
else:
    print(True)


