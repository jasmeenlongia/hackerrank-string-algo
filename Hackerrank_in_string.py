def hackerrankInString(s):
    for i in "hackerrank":
        if i in s:
            ind = s.index(i)
            s = s[ind+1:]
            #print(s)
        else:
            return "NO"
    return "YES"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)
