num='17'
j=1
k=0
h=0
primes=[]
random_num="" 
for k in range(len(num)-1):
 for i in range(1,len(num)):
    random_num= random_num+num[j]
    if j==len(num)-1 or j==0:
        j=0
        random_num= random_num+num[j]
        if k>0:
         j+=1
    else:
        j+=1
 #j=0
 if j==0 or j>1 :
  #print(random_num)
  if j>=2:
      j+=1
  else:
      j=2
  
  random_num=''
#random_num=int(random_num)
def circu_num(numb):
    h=0
    for l in range(1,numb+1):
       if numb%l==0:
           h+=1
    if h==2:
        primes.append(numb)
circu_num(5)
print(len(primes))
print(primes)
