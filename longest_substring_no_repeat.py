def longest_substring_no_repeat(s):
    """
    Return the length of the longest substring with no repeating characters.

    :type s: str
    :rtype: int
    """
    longest, start, encountered = 0, 0, {}
    for i in range(len(s)):
        if s[i] in encountered and start <= encountered[s[i]]:
            start = encountered[s[i]] + 1
        else:
            longest = max(longest, i - start + 1)
        encountered[s[i]] = i

    return longest

if __name__ == "__main__":
    print(longest_substring_no_repeat("abcabcbb"))
    print(longest_substring_no_repeat("bbbbb"))
    print(longest_substring_no_repeat("pwwkew"))
    print(longest_substring_no_repeat("c"))
    print(longest_substring_no_repeat("au"))