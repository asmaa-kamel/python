words=['aa','aab','cab','a','sss','ssss']
long=0
count=0
longList=[]

for word in words:
    count=0
    for i in word:
        count+=1
    if count >long:
        long=count    


for word in words:
    if len(word)==long:
        longList.append(word)
        
print("The longest words are :",longList)        