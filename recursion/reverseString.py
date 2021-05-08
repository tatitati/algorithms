
def reverseString(text, i):
    if(i >= len(text) / 2): return text
    else: 
        text[i], text[-1-i] = text[-1-i], text[i]
        return reverseString(text, i+1)

print(reverseString(list("hola"), 0))