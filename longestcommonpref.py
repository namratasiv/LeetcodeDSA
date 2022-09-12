def LCP(strs):    
    
    res = ""
        
    if(len(strs) == 1 or len(strs[0]) == 0):
        return strs[0]

    for n in range(len(strs[0])):   #iterating each letter in the first word
        
        res = res+strs[0][n]        #concatenating each letter to the result
        print(n,res)
        for i in strs[1:]:          #iterating each word in the list
            
            pre = i[0:n+1]          #getting the prefix of the word and comparing it to the result
            print(i,pre)
            if(res == pre):
                continue
            else:
                return res[:-1]
        
    return res
print(LCP(["flower","flow","flight"]))