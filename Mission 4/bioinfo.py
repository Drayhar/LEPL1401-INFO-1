"""
This program is made to do different operations on strings containing sequences of ADN
Theo-Time Bauvin & Vincent Bauffe, October 2019
"""
def is_adn(s):
    """
    This function verifies that all the characters from a given str is one of the following : a, t, c, g, A, T, C, G
    :param s: The sequence of ADN (str) that we want to verify
    :return: True if it is an ADN sequence, false in the other case
    """
    for i in s:
        if i in ["a", "t", "c", "g", "A", "C", "T", "G"]:
            state = True
        else:
            state = False
            break
    return state

def positions(s, p):
    """
    This function appeals to 2 str and check all the occurency of p in s
    :param s: long str
    :param p: Str to search for
    :return: A list with the positions of the occurencies of p in s
    """
    occurency = []
    p = p.lower()
    s = s.lower()
    for i in range(len(s)):
        if s[i:i+2] == p:
            occurency.append(i)
    return occurency

def distance_h(s, p):
    """
    This function compute the distance of Hamming
    :param s: str 1
    :param p: str 2
    :return: sum of letters differents
    """
    sum = 0
    if len(s) != len(p):
        return None
    for i in range(len(s)):
        if s[i] != p[i]:
            sum += 1
    return sum

def distances_matrices(l):
    """
    This function combine all the answers from distance_h for a list in a matrix
    :param l: list of str
    :return: matrix with sum of Hamming
    """
    list = []
    big_list = []
    for j in range(len(l)):
        for i in range(len(l)):
            list.append(distance_h(l[j], l[i]))
        big_list.append(list)
        list = []
    print(big_list)

def reverse_str(s):
    """
    Reverse a string
    :param s: string
    :return: string inversed
    """
    s1 = ""
    for i in s:
        s1 = i + s1
    return s1

def plus_long_palindrome(s):
    """
    find the biggest palindrome
    :param s: string
    :return: biggest palindrome
    """
    longest_str = ""
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i:j] == reverse_str(s[i:j]):
                new_str = s[i:j]
                if len(new_str) > len(longest_str):
                    longest_str = new_str
    return longest_str