def superReducedString(s):
    i=1
    while(i<len(s)):
        if s[i] == s[i-1]:
            s = s[0:i-1] + s[i+1:]
            i = 1
            if s == '':
                return "Empty String"
        else:
            i += 1
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
