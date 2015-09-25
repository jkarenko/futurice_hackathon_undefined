import zlib
import random

s = "a"
c = ""
while len(c) < 1024:
	c = zlib.compress(s, 9)
	s += chr(random.randint(0,255))

f = open('uncompr', 'w')
f.write(c)