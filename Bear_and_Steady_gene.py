def steadyGene(x, gene):
    countreq = x//4
    dict = {'A' : 0, 'T' : 0, 'C' :0 , 'G' :0 }
    for i in gene:
        dict[i] += 1

    if dict['A'] == countreq and dict['T'] == countreq and dict['C'] == countreq and dict['G'] == countreq:
        return 0
    
    high = 0
    low = 0
    length = x
    while high < x and low < x:
        while (dict['A'] > countreq or dict['C'] > countreq or dict['T'] > countreq or dict['G'] > countreq) and high < x:
            dict[gene[high]] -= 1
            high += 1
        while dict['A'] <= countreq and dict['C'] <= countreq and dict['T'] <= countreq and dict['G'] <= countreq:
            dict[gene[low]] += 1
            low += 1
        if high - low < length :
            length = high - low + 1
    return length

def solve():

    n = int(input())

    gene = input()

    result = steadyGene(n, gene)

    print(result)

solve()
