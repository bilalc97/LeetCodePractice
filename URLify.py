def urlify(s, size):
    """
    Modify s so that it replaces all spaces with a "%20".

    :param s:
    :param size:
    :return:
    """
    i = 0
    queue = []
    while i < len(s):
        if s[i] == " " and i < size:
            queue.extend(["%", "2", "0"])
        if len(queue) != 0:
            print(i)
            if s[i] != " ":
                queue.append(s[i])
            s[i] = queue.pop(0)
        i += 1


if __name__ == "__main__":
    string1 = ["C", "o", "c", "o", "a", " ", "B", "e", "a", "n", "s", " ", "O", "n", " ", " ", " ", " "]
    urlify(string1, len(string1))
    print(string1)
