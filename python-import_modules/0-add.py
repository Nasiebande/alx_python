#!/usr/bin/python3
a = 1
b = 2

add_code = '''
def add(a, b):
    return a + b
'''

exec(add_code)

print("{} + {} = {}".format(a, b, add(a, b)))
