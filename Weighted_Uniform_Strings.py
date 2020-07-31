def weightedUniformStrings(s, queries):

    seq=[]
    for num in range(1,27):
        seq.append(0)

    for x in sorted(set(s)):
        i = 1;
        while x * i in s:
            i += 1
        seq[ord(x)-97]=i-1 

    finale=set()              

    for index,every in enumerate(seq):
        for sval in range(every):
            finale.add((index+1)*(sval+1)) 

    for x in queries:
        print("Yes" if x in finale else "No")

def solve():
    s = input().strip()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    weightedUniformStrings(s, queries)

solve()
