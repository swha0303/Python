# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

rule = """외래어 표기법 
제1장 표기의 기본 원칙 
제1항 외래어는 국어의 현용 24 자모 만으로 적는다. 
제2항 외래어의 1 음운은 원칙적으로 1 기호로 적는다. 
제3항 받침에는 'ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ'만을 쓴다. 
제4항 파열음 표기에는 된소리를 쓰지 않는 것을 원칙으로 한다. 
제5항 이미 굳어진 외래어는 관용을 존중하되, 그 범위와 용례는 따로 정한다."""
number = rule.index('외')
print(rule)
print(rule.count('외래어'))
print(rule.find('외'))
print(rule.index('외'))
print(f"{number-1}")
print(rule.replace('외래어', '한국어'))