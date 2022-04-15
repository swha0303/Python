# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num = int(input("연도를 입력하세요: "))
if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0 :
	print("%d년은 윤년입니다." %num)
else:
	print("%d년은 윤년이 아닙니다." %num)

	

