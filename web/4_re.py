import re



def print_match(m):
    if m:
        print("m.group()",m.group()) #일치하는 문자열
        print("m.string()",m.string) #입력받은문자열
        #m.start() 일치하는 문자열의 시작인덱스
        #m.end() 일치하는 문자열의 끝 인덱스
        #m.span() 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("매칭되지 않았습니다.")


p=re.compile("ca.e")
#.은 하나의 문자를 의미
m=p.match("case")

s=p.search("good care")#서치는 일치하는게 있는지 확인
print_match(s)

f=p.findall("carelesscafe")
print(f)

p1=re.compile("\d\D")
s1=p1.search("0d002")
print(s1.group())
