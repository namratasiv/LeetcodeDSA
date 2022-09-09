
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
result = []
        
for i in range(len(transactions)-1):
    temp=str(transactions[i].split(","))
    temp_next = str(transactions[i+1].split(","))
    print(temp)
    #print(int(float(temp[2])))
    if (int(temp[2]) > 1000) or (int(temp_next[1])-int(temp[1]) < 60 and temp[0] == temp_next[0] and temp[3] != temp_next[3]):
        result.append(transactions[i])
print(result)