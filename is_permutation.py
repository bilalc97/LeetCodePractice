def is_permutation(s1, s2):
    """
    Return True is s1 and s2 are permutations of each other and False otherwise.

    :param s1: str
    :param s2: str
    :return: bool
    """
    if len(s1) != len(s2):
        return False
    else:
        s1_dict = {}
        for i in range(len(s1)):
            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1

        for i in range(len(s2)):
            if s2[i] in s1_dict and s1_dict[s2[i]] > 0:
                s1_dict[s2[i]] -= 1
            else:
                return False

        for key in s1_dict.keys():
            if s1_dict[key] != 0:
                return False

        return True

if __name__ == "__main__":
    print(is_permutation("abcdefghijklmno", "onmlkjihgfedcba"))
    print(is_permutation("hello", "helo"))