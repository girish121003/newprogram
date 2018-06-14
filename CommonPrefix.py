def longestCommonPrefix(strs):
    if not strs: return ''
    first = min(strs)
    for i in range(len(first)):
        for s in strs:
            if s[i] != first[i]:
                return first[:i] if i > 0 else ''
    return first


strs=[y for y in input().split()]

result=longestCommonPrefix(strs)
print(result)


