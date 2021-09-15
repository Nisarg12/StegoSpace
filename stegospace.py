#!/usr/bin/python

import re

f = open('steg_file.txt')
lines = [x[:-1] for x in f.readlines()]
f.close()

hidden_msg = []
for line in lines:
    inv = re.findall(r"(\s+)", line)
    if inv:
        # Try both of these substitutions for constructing binary values.
        inv = int(''.join(inv).replace(' ', '0').replace('\t', '1'), 2)
        # inv = int(''.join(inv).replace(' ','1').replace('\t','0'),2)
        if inv in range(255):
            hidden_msg.append(chr(inv))

print(''.join(hidden_msg))
