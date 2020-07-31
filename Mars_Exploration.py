def marsExploration(s):
    changes = 0
    for i in range(len(s)):
        if i%3 == 0 or i%3 == 2:
            if s[i] != 'S':
                changes += 1
        elif 1%3 == 1:
            if s[i] != 'O':
                changes += 1
    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
