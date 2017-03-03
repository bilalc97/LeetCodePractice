def longest_palindromic_substring(s):
    """
    Return the longest palindromic substring in s.

    :type s: str
    :rtype: str
    """
    longest = s[0] if len(s) > 0 else ""
    for i in range(len(s)):
        j = len(s)
        while s[i] in s[i+1:j] and j <= len(s):
            j = s[i + 1:j].rfind(s[i]) + i + 2
            print(i, j)
            if is_palindrome(s[i:j]) and len(longest) < len(s[i:j]):
                longest = s[i:j]
                j = len(s) + 1
            else:
                j -= 1
        if len(s) - len(longest) <= i:
            break
    return longest


def is_palindrome(sub):
    """
    Return True if sub is palindromic, False otherwise.

    :type sub: str
    :rtype: bool
    """
    for i in range(len(sub)):
        if sub[i] != sub[len(sub) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("dad"))
    print(is_palindrome("cat"))

    print(longest_palindromic_substring("babad"))
    print(longest_palindromic_substring("cbbd"))
    print(longest_palindromic_substring("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbggggggggggggggggggggggggggggggggggggggggggg"))