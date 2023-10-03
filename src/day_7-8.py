def palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.

    :param s: Input string
    :return: True if palindrome, and False if not.
    """
    s = s.replace(" ", "")
    return s == s[::-1]
    
print(palindrome("racecar"))
print(palindrome("Hello"))
