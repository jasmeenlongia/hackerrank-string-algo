def upper_digits(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count

def camelcase(s):
    ans = upper_digits(s)
    return ans + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
