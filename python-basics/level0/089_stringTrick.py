# 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 
# 문자열 rnyString이 주어질 때, rnyString의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항) 1 ≤ rnyString의 길이 ≤ 100 , rnyString은 영소문자로만 이루어져 있습니다.

def solution(rnyString):
    return rnyString.replace("m", "rn")

print(solution("masterpiece"))
print(solution("programmers"))
print(solution("jerry"))
print(solution("burn"))