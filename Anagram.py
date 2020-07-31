def anagram(s):
    l = len(s)
    if l%2 != 0:
        return "-1"

    mid = l//2

    str1 = s[0:mid]
    str2 = s[mid:l]

    changes = 0

    set1 = set(str1)

    for i in set1:
        c1 = str1.count(i)
        c2 = str2.count(i)
        if c1 > c2:
            changes += c1 - c2

    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
