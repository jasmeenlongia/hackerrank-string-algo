def num_there(s):
    return any(i.isdigit() for i in s)

def upper_there(s):
    return any(i.isupper() for i in s)

def lower_there(s):
    return any(i.islower() for i in s)

def has_special_char(s):
    return any(i in '!@#$%^&*()-+' for i in s)

def minimumNumber(n, password):
    req = 0

    if num_there(password) == False:
        req += 1

    if upper_there(password) == False:
        req += 1
    
    if lower_there(password) == False:
        req += 1

    if has_special_char(password) == False:
        req += 1

    if len(password) + req < 6:
        req += 6 - len(password) - req

    return(req)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
