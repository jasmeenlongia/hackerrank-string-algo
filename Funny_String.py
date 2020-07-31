def palindrome(seq):
    return seq == seq[::-1]

def funnyString(s):
    ascii = []
    for i in s:
        ascii.append(ord(i))
    diff = []

    for i in range(len(ascii)-1):
        diff.append(abs(ascii[i+1] - ascii[i]))
    
    if palindrome(diff) == True:
        return "Funny"

    return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
