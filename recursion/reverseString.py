
def reverseString(text, i):
    if(i >= len(text) / 2): return text
    else: 
        text[i], text[-1-i] = text[-1-i], text[i]
        return reverseString(text, i+1)

print(reverseString(list("hola"), 0)) # ['a', 'l', 'o', 'h']



def reverseString2(text):    
    if len(text) == 0 or len(text) == 1: return text
    else:         
        return text[-1:] + reverseString2(text[:-1])

print(reverseString2(list("hola"))) # ['a', 'l', 'o', 'h']


