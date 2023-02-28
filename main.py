def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


original_list = [[[1, 2], 3], [4], [5, 6], [7, [8, 9]]]
print('Original List', original_list)
print('Transformed Flat List', flatten(original_list))
