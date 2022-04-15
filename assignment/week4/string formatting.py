# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

year = str(input())
month = str(input())
date = str(input())
day = str(input())

print("오늘은 {0}년 {1}월 {2}일 {3}입니다.".format(year, month, date, day))

'''
Format
Print("{0} {1} {2} {1}".format(a, b, c, d)) -> a b c a 각각의 내용
Print(f"{a} {b} {c}") -> 앞에서 포맷은 중괄호안 변수 이름
Print("%d %f " %(a, b))처럼 사용해야함.(컴마 없다!!) 


예외:format에서 변수 선언
-> print("{name}의 반은 {class}반이고 {0}의 반은 {1}반이다.".format(이여름, 2, name="김가을", class=3))
-> 0, 1순서 값 다 적고 변수 선언해야됨 (format(이여름, class=3, 2, name="김가을")안된다는 말)

->{num+1} = num의 수 + 1
'''

