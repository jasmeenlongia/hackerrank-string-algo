def gameOfThrones(s):
    unique = set(s)
    if len(s)%2 == 0:
        for i in unique:
            c = s.count(i)
            if c%2 != 0:
                return "NO"
    else:
        odd = 0
        for i in unique:
            c = s.count(i)
            if c%2 != 0:
                odd += 1
                if odd > 1:
                    return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
