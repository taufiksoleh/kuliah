


def is_palindrome_v1(s):
        """
        (str) -> bool

        Return True if and only if s is a palindrome.

        >>> is_palindrome_v1('noon')
        True
        >>> is_palindrome_v1('racecar')
        True
        >>> is_palindrome_v1('danted')
        False
        """

        return reverse(s) == s


def reverse(s):
        """
         (str) -> str
        Return s reversed

        >>> reverse('hello')
        'olleh'

        >>> reverse('a')
        'a'
        """

        rev = ''

        # for each charatcer in s, add that char to the beginning of rev.
        for ch in s:
                rev = ch + rev

        return rev
