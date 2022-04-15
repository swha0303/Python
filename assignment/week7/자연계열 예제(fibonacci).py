# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

calc = True

while calc:
	fib1 = 1
	fib2 = 1
	
	num = int(input('3 이상의 정수를 입력합니다. 3 미만의 수를 입력하면 종료됩니다: '))
	
	if num < 3:
		print('종료합니다.')
		calc = False
	else:
		for i in range(1, num+1):
			if i == 1:
				print("{0}번 피보나치 수는 {1}입니다.".format(i, fib1))
			elif i == 2:
				print("{0}번 피보나치 수는 {1}입니다.".format(i, fib2))
			else:
				print("{0}번 피보나치 수는 {1}입니다".format(i, fib1+fib2))
				tmp = fib2
				fib2 = fib1 + fib2
				fib1 = tmp
				
	
				
						
				
				