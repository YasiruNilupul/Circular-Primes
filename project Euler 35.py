#num='242342425'
j=1
primes=[]
#random_num=0
for num in range(110,111):
    #random_num="" 
    num=str(num)
    for k in range(len(num)-1):
     random_num=''
     
     for i in range(1,len(num)):
        #print("we")
        random_num= random_num+num[j]
        if j==len(num)-1 or j==0:
            j=0
            random_num= random_num+num[j]
            if k>0:
             j+=1
        else:
            j+=1                        
     if j==0 or j>1 :
       #print(random_num)
     
       h=0
       random_num=int(random_num)
       for l in range(1,random_num+1):
        if random_num%l==0:
           h+=1
       if h==2:
         primes.append(random_num)

      
      
       if j>=2:
         j+=1
       if len(num)==2:
         j=1
       elif len(num)>=3:
         j=2
print(j)
print(len(primes))
print(primes)
#print(j)
#print(primes)
