

L, C = map(int, input().split())
candidate = input().split()
vowel_set = {'a', 'e', 'i', 'o', 'u'}
vowels = []
consonants = []


n = 0
r = 0
sel = list()




for i in candidate:
    if i in vowel_set:
        vowels.append(i)
    else:
        consonants.append(i)

def combination(idx, sidx, candidate_list):
    global res
    if sidx == r:
        res += [sel]
        #print(sel)
        return

    if idx == n:
        return

    sel[sidx] = candidate_list[idx]
    combination(idx+1, sidx+1, candidate_list)
    combination(idx+1, sidx, candidate_list)

for i in range(1, len(vowels)+1, 1):

    res = []

    n = len(vowels)
    r = i
    sel = [0] * r
    combination(0, 0, vowels)

    print(res)
    
    # n = len(consonants)
    # r = L-i
    # sel = [0] * r
    # combination(0, 0, consonants)

    #res.sort()
    #print(res)
    


