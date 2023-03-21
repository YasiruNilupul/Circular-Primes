num='197'
random_num=""
for i in range(0,len(num)+1):
    random_num=num.replace(num[i],num[i+1])
    #random_num=num.append(num[0])

print(random_num)