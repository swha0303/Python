# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

while True:
	print("1. 더하기")
	print("2. 빼기")
	print("3. 곱하기")
	print("4. 나누기")
	print("5. 프로그램 종료")
	menu = int(input("원하는 기능의 번호를 입력하세요: "))
	if menu == 5 or (menu > 5 or menu <0):
		if menu == 5:
			print("프로그램을 종료합니다.")
			break
		else:
			print("잘못된 번호입니다.")
			continue
	num1 = int(input("첫 번째 정수를 입력하세요:"))
	num2 = int(input("두 번째 정수를 입력하세요:"))
	if menu == 1:
		print("{0}와 {1}를 더하기 연산한 결과는 {2}입니다.".format(num1, num2, num1+num2))
	elif menu == 2:
		print("{0}에서 {1}를 빼기 연산한 결과는 {2}입니다.".format(num1, num2, num1-num2))
	elif menu == 3:
		print("{0}와 {1}를 곱하기 연산한 결과는 {2}입니다.".format(num1, num2, num1*num2))
	elif menu == 4:
		if num2 == 0:
			print("연산이 불가합니다.")
			continue
		div = num1/num2
		print("%d를 %d로 나누기 연산한 결과는 %.6f입니다." %(num1, num2, div))
	else:
		print("잘못된 번호입니다.")
		continue
	