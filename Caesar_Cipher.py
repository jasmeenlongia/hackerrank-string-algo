def caesarCipher(s, k):
    newstr = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                ascii_val = 97
            elif i.isupper():
                ascii_val = 65
            newstr += chr((ord(i) - ascii_val + k) % 26 + ascii_val)
        else:
            newstr += i
    return newstr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
