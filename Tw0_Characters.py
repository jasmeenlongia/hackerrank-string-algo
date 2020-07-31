def validate(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True
    
def alternate(str):
    s = ''
    maxlen = 0
    unique = list(set(str))
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            #print('removing', unique[i], unique[j])
            for z in str:
                if z == unique[i] or z == unique[j]:
                    s = s + z
            #print(s, len(s))
            l = len(s)
            if validate(s) == True:
                if l > maxlen:
                    maxlen = l
            s = ''
    return maxlen


if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(result)
