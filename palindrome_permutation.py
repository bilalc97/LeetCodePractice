def palindrome_permutation(s):
    """
    Return True is string s is a permutation of a palindrome and False otherwise.

    :param s:
    :return:
    """
    chars = {}
    spaces = 0
    for char in s:
        if char in chars:
            chars[char] += 1
        elif char == " ":
            spaces += 1
        else:
            chars[char] = 1

    if (len(s) - spaces) % 2 == 0:
        for key in chars:
            if chars[key] % 2 != 0:
                return False
    else:
        odd_found = False
        for key in chars:
            if chars[key] % 2 == 0:
                if odd_found:
                    return False
                else:
                    odd_found = True

    return True

if __name__ == "__main__":
    print(palindrome_permutation("Tact Coa"))