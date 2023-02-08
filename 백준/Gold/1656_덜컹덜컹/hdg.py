import sys
input = sys.stdin.readline

[INDEX, LENGHT] = [0, 1]

def getAngle(t, a, b):
   		return min((t + a - b) % t, (t + b - a) % t)

while True:
	t = int(input())
	if t == 0:
		break
	info = [int(input()) for _ in range(t)]

	def isPossible(length):
		points = list(filter(lambda item: item[LENGHT] >= length, enumerate(info)))
		maxAngle = 0
		sum = 0
		for index in range(len(points)):
			point1 = points[index]
			point2 = points[(index + 1) % len(points)]
			angle = getAngle(t, point1[INDEX], point2[INDEX])

			sum += angle
			maxAngle = max(maxAngle, angle)
		return (sum == t) and not (2 * maxAngle == t)

	[left, right] = [min(info), max(info)]

	answer = left
	while left <= right:
		mid = (left + right) // 2
		if isPossible(mid):
			answer = mid
			left = mid + 1
		else:
			right = mid - 1
	
	print(sum(map(lambda item: 0 if answer >= item else item - answer, info)), end="\n\n")