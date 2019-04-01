# String Permutation
def permutation(a):
    if not a:
        return []
    if len(a) == 1:
        return [a]
    result = []
    for i in range(len(a)):
        for j in permutation(a[:i] + a[i+1:]):
            result.append(a[i] + j)
    return result
