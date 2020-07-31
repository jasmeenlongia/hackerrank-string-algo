def gemstones(arr):
    similar = set(arr[0])
    for i in range(1, len(arr)):
        similar = similar.intersection(arr[i])
    return len(similar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
