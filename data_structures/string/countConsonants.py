def countConsonantsIterative(text):
    acc = 0
    for i in text:
        if i not in ['A', 'E', 'I', 'O', 'U'] and i not in ['a', 'e', 'i', 'o', 'u']:
            acc += 1

    return acc



print(countConsonantsIterative(list("hello")))
