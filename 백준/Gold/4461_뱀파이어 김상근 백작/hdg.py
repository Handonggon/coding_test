import sys
input = sys.stdin.readline

cube = [pow(num, 3) for num in range(4001)]
cubeRoot = {cube : i + 1 for (i, cube) in enumerate(cube[1:])}

while True:
	num = int(input())
	if num == 0:
		break
	
	ok = False
	for b in range(1, 2000):
		res = num * cube[b]
		for a in range(1, 4000 - (2 * b)):
			dif = res - cube[a]
			if dif in cubeRoot:
				c = cubeRoot[dif]
				if a + c + (2 * b) < 4000:
					ok = True
					break
		if ok:
			break
	print("({0}/{1})^3 + ({2}/{1})^3 = {3}".format(max(a, c), b, min(a, c), num)) if ok else print("No value.")