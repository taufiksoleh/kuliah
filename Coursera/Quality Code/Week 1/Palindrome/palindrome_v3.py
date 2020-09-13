


def is_palindrome_v3(s):
        """
        (str) -> bool

        Return True if and only if s is a palindrome.

        >>> is_palindrome_v3('noon')
        True
        >>> is_palindrome_v3('racecar')
        True
        >>> is_palindrome_v3('danted')
        False
        """

        # s[i] and s[j] are the next pair of character to compare
        i = 0
        j = len(s) - 1

        # The character in s[:i] have been successfully compared to those in s[j:].
        while i < j and s[i] == s[j]:
            i = i + 1
            j = j - 1

        # If we exited because we successfully compared all pairs of characther,
        # then j <= i
        return j <= i
        

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
