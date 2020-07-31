def theLoveLetterMystery(s):
    l = len(s)
    op = 0
    for i in range(l//2):
        op = op + abs(ord(s[i]) - ord(s[l-i-1]))
    return op
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
