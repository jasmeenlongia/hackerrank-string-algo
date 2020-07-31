def sherlockAndAnagrams(s):
    ans = 0
    res = [''.join(sorted(s[i: j])) for i in range(len(s))for j in range(i + 1, len(s) + 1)] 
    unique = set(res)
    for i in unique:
        c = res.count(i)
        ans += int(c * (c-1) / 2)

    return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
