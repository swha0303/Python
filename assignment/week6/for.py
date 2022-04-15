# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())
sum = 0

for i in range(0, num+1, 1):
	if i % 2 == 0:
		sum += i

print(sum)

'''
1. for i in list
-> list의 값을 순차적으로 i에 대입해가며 반복(list안의 요소 개수만큼 반복)

2. range함수의 사용
a, range(n)
-> 0부터 n까지 생성
b. range(a, b)
-> a<=x<b까지 반복 a, a+1, ... b-1까지(개수는 b-a)
c. range(a, b, k)
-> a<=x<b까지 반복하는데 k만큼을 간격으로 지정한다. a, a+k, ... b-1까지
※k는 음수값도 가능하다.
'''
