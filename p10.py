def stuff(km, g, f):
	def lcm(a,b):
		for i in range(1,a*b):
			if i % a == 0 and i % b == 0:
				return i
		return a*b

	# Inclusion exclusion fuck yeah
	result = km / g + km / f - km / lcm(f,g)

	if km % g == 0 or km % f == 0:
		return result - 1
	return result

print stuff(10, 9, 1)