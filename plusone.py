class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        s = str(digits).replace(",","").replace("[","").replace("]","").replace(" ","")
        n = int(s) + 1
        res = "".join(str(n))
        
        return list(res)