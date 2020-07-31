def palindrome(s): 
    return s == s[::-1] 

def palindromeIndex(s):
    if palindrome(s) == True:
        return -1
    length = len(s)
    for i in range(length//2 + 1):
        if s[i] != s[length-i-1]:
            str = s[0:i] + s[i+1:length]
            if palindrome(str) == True:
                return i
            str = s[0:length-i-1] + s[length-i:length]
            if palindrome(str) == True:
                return length - i - 1
    return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
