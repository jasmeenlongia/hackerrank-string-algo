def isValid(s):
    
    c = []
    odd = 0
    str = set(s)
    for i in str:
        #print(i)
        #print(s.count(i))
        c.append(s.count(i))
    #print(c)
    distinct = set(c)
    #print(distinct)
    if len(distinct) == 1:
        return "YES"
    if len(distinct) > 2:
        return "NO"
    if len(distinct) == 2:
        for j in distinct:
            #print(j)
            if c.count(j) > 1:
                odd += 1
                #print("odd is", odd)
                if odd >= 2:
                    return "NO"
        if c.count(max(distinct)) > 1 and c.count(min(distinct)) == 1:
            return "YES"
        if c.count(max(distinct)) == 1 and c.count(min(distinct)) >= 1:
            if max(distinct)-min(distinct) == 1:
                return "YES"

    return "NO"

if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result)
