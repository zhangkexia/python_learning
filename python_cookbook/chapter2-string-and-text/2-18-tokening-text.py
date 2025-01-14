# 单引号里的特殊符号都是原语义的。
text = 'foo = 23 + 42 * 10'
print(text)

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

print(tokens)

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
# print('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner = master_pat.scanner('foo = 42')
# scanner.match()

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
# 正则匹配扫描。



