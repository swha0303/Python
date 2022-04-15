# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num1 = 17.5
num2 = 10
cpx1 = 3 + 3j
cpx2 = 1 - 2j
str1 = "Hello"
str2 = "goorm"

print(num1+num2, type(num1+num2))
print(str1+str2, type(str1+str2))
print(num1+cpx1, type(num1+cpx1))
print(num1*num1, type(num1*num1))
print(num1/num2, type(num1/num2))
print(num1//num2, type(num1//num2))
print(num1%num2, type(num1%num2))
print(cpx1/cpx2, type(cpx1/cpx2))

#복소수 관련 연산
'''
A = 3j + 1
-> A.imag 허수부 / A.real 실수부 / A.conjugate() 켤레복소수
-> 결과값은 각각 3, 1, 3j-1
위의 따옴표 세개는 문자열을 처리할때는 물론 주석으로도 쓰인다.

'''
