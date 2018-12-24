def solution(A):
	b = A.sort()
	test = 1
	count = 0
	while count <= len(A):
		if test in A:
			test += 1
		count += 1

	return test

x = [1, 5, 3, 2, 5, 7, 3]
soln = solution(x)
print(soln)