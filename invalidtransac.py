
transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
result = []
        
for i in range(1, len(transactions)):
    temp=transactions[i-1].split(",")
    temp_next = transactions[i].split(",")
    print(temp,temp_next)
    if (int(temp[2]) > 1000):
        result.append(transactions[i-1])
    if (int(temp_next[2]) > 1000):
        result.append(transactions[i])
    if (int(temp_next[1])-int(temp[1]) <= 60 and temp[0] == temp_next[0] and temp[3] != temp_next[3]):
        result.append(transactions[i-1])
        result.append(transactions[i])

print(result)