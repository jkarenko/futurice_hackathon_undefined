def do_shit(key, msg):
	mf = {x[1]:x[0] for x in zip([chr(x) for x in range(65,91)], [x for x in key[::-1]])}
	return "".join([ mf[x] if x in mf else " " for x in msg])

print do_shit("QWERTYUIOPASDFGHJKLZXCVBNM", "TCOW ICBOCU FCIIMZC")