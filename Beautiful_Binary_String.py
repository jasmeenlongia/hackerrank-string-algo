def beautifulBinaryString(s):
    if "010" not in s:
        return 0
    else:
        s = s.replace("010", 'x')
        c = s.count('x')
        return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
