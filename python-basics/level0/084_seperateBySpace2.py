# 단어가 공백 한 개 이상으로 구분되어 있는 문자열 myString이 매개변수로 주어질 때, 
# myString에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항
# myString은 영소문자와 공백으로만 이루어져 있습니다.
# 1 ≤ myString의 길이 ≤ 1,000
# myString의 맨 앞과 맨 뒤에도 공백이 있을 수 있습니다.
# myString에는 단어가 하나 이상 존재합니다.

def solution(myString):
    return myString.split()

print(solution(" i    love  you"))
print(solution("    programmers  "))