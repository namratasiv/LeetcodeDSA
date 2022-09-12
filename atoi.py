s = "words and 987"
#s = "  -42"
if s[0].isalpha():
    print(0) 
s = ''.join(letter for letter in s if not letter.isalpha())
        
s = s.strip(" ")
print(s[0])

print(int(s))