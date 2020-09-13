


def is_palindrome_v2(s):
        """
        (str) -> bool

        Return True if and only if s is a palindrome.

        >>> is_palindrome_v2('noon')
        True
        >>> is_palindrome_v2('racecar')
        True
        >>> is_palindrome_v2('danted')
        False
        """

        # The number of charts is s
        n = len(s)

        #Compare the first half of s to the reversee if the second half.
        #Omit the middle character of an odd-length string.
        return s[:n // 2] == reverse(s[n - n //2:])


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
