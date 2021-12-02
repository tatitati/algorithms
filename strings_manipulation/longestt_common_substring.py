txt1 = 'academy'
txt2 = 'abracadabra'


# force brute
def findCommonSubstring(txt1, txt2):
    previousAcc = ""
    currentAcc = ""

    for i in range(len(txt1)):
        for j in range(len(txt2)):
            if txt1[i] == txt2[j]:
                currentAcc.append(txt2[j])
                match = True


        if len(currentAcc) > previousAcc:
            previousAcc = currentAcc
            currentAcc = ""

    return previousAcc
