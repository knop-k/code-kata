# https://www.codewars.com/kata/5412509bd436bd33920011bc
# Solution:
def maskify(cc):
    if len(cc) > 4:
        cc = ( '#' * (len(cc)-4) ) + cc[-4:]
    return cc
