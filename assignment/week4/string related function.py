# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

sentence = "Contrary to popular belief, Lorem Ipsum is not simply random text."

num1 = sentence.count('t')
print(num1)

num2 = sentence.find('i')
print(num2)

print(sentence.upper())
print(sentence.lower())
print(sentence.replace('a', 'b'))

'''
a.count("b") ->문자열 변수 a에서 "b"의 갯수
a.find("b") ->문자열 변수 a에서 "b"가 처음 발견된 위치 반환(0부터 센다.)※문자없을시 -1 &리스트 튜플, 딕셔너리 이용불가능
a.index("b")->문자열 변수 a에서 "b"가 처음 발견된 위치 반환(0부터 센다.)※문자없을시 에러 & 리스트, 튜플에서 이용가능 딕셔너리 이용불가
a.upper()/a.lower() ->문자열을 모두 대문자/소문자 변환
a.strip()/a.lstrip()/a.rstrip() ->각각 공백제거/왼쪽 공백 제거/오른쪽 공백 제거
replace("a", "b") ->"a"를 "b"로 바꿔라
'''
