def makingAnagrams(s1, s2):
    deletion = 0
    similar = ''
    set1 = set(s1)
    set2 = set(s2)

    for i in set1:
        if i not in set2:
            deletion += s1.count(i)
        else:
            similar += i
    for i in set2:
        if i not in set1:
            deletion += s2.count(i)

    for i in similar:
        c1 = s1.count(i)
        c2 = s2.count(i)
        if c1 != c2:
            deletion += abs(c1 - c2)
    
    return deletion

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)
