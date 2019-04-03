def permutation(a):
    """string permutation"""
    if not a:
        return []

    if len(a) == 1:
        return [a]

    result = []
    for i in range(len(a)):
        for item in permutation(a[:i] + a[i+1:]):
            result.append(a[i] + item)
    return result


if __name__ == "__main__":
    print permutation('abc')
