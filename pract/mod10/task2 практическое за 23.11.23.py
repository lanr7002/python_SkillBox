import re

def correct_color(color):

    """
>>> correct_color("#21f48D")
    True
    >>> correct_color("#888")
    True
    >>> correct_color("rgb(255, 255, 255)")
    True
    >>> correct_color("rgb(10%, 20%, 0%)")
    True
    >>> correct_color("hsl(200, 100%, 50%)")
    True
    >>> correct_color("hsl(0, 0%, 0%)")
    True
    >>> correct_color("#2345")
    False
    >>> correct_color("ffffff")
    False
    >>> correct_color("rgb(257, 50, 10)")
    False
    >>> correct_color("hsl(20, 10, 0.5)")
    False
    >>> correct_color("hsl(34%, 20%, 50%)")
    False
    """
    color_checker = re.compile(
        r'^#(?:[0-9a-fA-F]{3}){1,2}$|rgb\((\d{1,2}%?|1\d{2}|2[0-4]\d|25[0-5]),\s*(\d{1,2}%?|1\d{2}|2[0-4]\d|25[0-5]),\s*(\d{1,2}%?|1\d{2}|2[0-4]\d|25[0-5])\)$|hsl\((\d{1,3}),\s*(\d{1,3}%?),\s*(\d{1,3}%?)\)$')
    return bool(color_checker.match(color))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
