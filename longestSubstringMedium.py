'''Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.'''

def get_longest_substring_length(string):
    store = {}
    ret = start = idx = 0 # we need to initialize idx now in case of an empty string
    for idx, char in enumerate(string, 1):  # zero-based index complicates substring length calculation. we also might use idx to get full string length
        if char in store and start <= store[char]:
            start = store[char]
        store[char] = idx
        ret = max(ret, idx-start) # we only need to store the longest substring length
    return ret or idx # if no substrings were found, we assume full string length


s=input("Enter the string : ")
k=get_longest_substring_length(s)
print(k)