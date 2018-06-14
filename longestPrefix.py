def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]

    min_word = min(strs)

    for i in range(len(min_word)):
        t = min_word[i]
        for word in strs:
            if t != word[i]:
                return min_word[0:i]
    else:
        return min_word

k=[x for x in input().split()]
j=longestCommonPrefix(k)
print(j)









# input_string=[x for x in input().split()]
# count=0
# inc=0
# minnum=min(input_string)
#
# for x in range(len(minnum)):
#     t=minnum[x]
#     for y in input_string:
#         if t!=y[x]:
#             print(input_string[0:x])