def printmat(mat):
	for x in mat:
		print x

def repeats(st):
	mat = [[0] * len(st) for x in range(len(st))]

	for x in range(0,len(st)-1):
		for y in range(0, len(st)-1):
			if st[x] == st[y]:
				mat[y+1][x+1] = mat[y][x] + 1
			else:
				mat[y+1][x+1] = 0

	candidates = [sum([i > 0 for i in x]) for x in mat]
	print candidates
	m = max(candidates)
	mrow = 0
	for i in range(len(candidates)):
		if candidates[i] == m:
			a = min([x for x in mat[i] if x > 0])
			if mrow < a:
				mrow = a

	for i in range(len(candidates)):
		if candidates[i] == m and min([x for x in mat[i] if x > 0]) == mrow:
			for j in range(len(mat[i])):
				if mat[i][j] > 0:
					pass
					#print st[j-mrow:j]

	#printmat(mat)

repeats("banana")