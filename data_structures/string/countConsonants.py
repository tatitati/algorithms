def countConsonantsIterative(text):
    acc = 0
    for i in text:
        if i not in ['A', 'E', 'I', 'O', 'U'] and i not in ['a', 'e', 'i', 'o', 'u']:
            acc += 1
    return acc

print(countConsonantsIterative(list("hello"))) # 3






def countConsonantsRecursive(text):
    print(text)
    if len(text) <= 1:    
        return 1 if text[0] not in ['A', 'E', 'I', 'O', 'U'] and text[0] not in ['a', 'e', 'i', 'o', 'u'] else 0    

    if text[0] not in ['A', 'E', 'I', 'O', 'U'] and text[0] not in ['a', 'e', 'i', 'o', 'u']:
        return  1 + countConsonantsRecursive(text[1:])
    else:
        return  0 + countConsonantsRecursive(text[1:])
    
print(countConsonantsRecursive(list("hello"))) # 3
