# https://www.codewars.com/kata/55908aad6620c066bc00002a
# Solution:
def xo(s):
    s = s.lower()
    # it can work without this statement
    if 'x' not in s and 'o' not in s:
        return True
    ###################################
    return s.count('x') == s.count('o')
