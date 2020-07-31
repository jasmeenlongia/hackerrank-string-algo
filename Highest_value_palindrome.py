highest value palindrome 

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    if n == 1:
        return "9"
    diff = 0
    index = [False for i in range(n//2)]
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            index[i] = True
            s[i] = max(s[i], s[n - i - 1])
            s[n - i - 1] = max(s[i], s[n - i - 1])
            diff += 1
    if diff > k:
        return "-1"
    if diff < k:
        changesleft = k - diff
        for i in range(0, n//2):
            if changesleft - 2 >= 0 and index[i] == False:
                if s[i] != '9':
                    s[i] = '9'
                    s[n - i - 1] = '9'
                    changesleft -= 2
            elif changesleft - 1 >= 0 and index[i] == True:
                if s[i] != '9':
                    s[i] = '9'
                    s[n - i - 1] = '9'
                    changesleft -= 1
        if changesleft > 0 and n%2 != 0:
            s[(n//2)] = '9'
            
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = list(input())

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
