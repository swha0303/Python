# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

start_day = 2  # Tuesday
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')
for j in range(2): # 0~2
	print('\t', end='')
for i in range(1, 32): # 1~31
	if (i % 7) != 5:
		print('\t%d' %i, end='')
	elif (i % 7) == 5:
		print('\t%d\n' %i)


'''
print함수에서의 옵션
sep="k"
->print("a","b","c", sep="k")일때,akbkc
->콤마로 연결할때 기본 사이값은 공백이다. 이걸 조정할때 sep을 사용한다.
->sep="" 사용시 공백값이 사라져서 +를 사용하지 않아도 붙여서 출력된다.
end="k"
->print("aaaaa", end="k")일때, aaaaak
->출력하고 난 뒤 기본 마지막값은 개행문자이다. 이걸 조정할때 end를 사용한다.
->end="" 사용시 print 출력을 했을때 개행을 막을 수 있다.
'''
