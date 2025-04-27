# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# 1 ≤ is_suffix의 길이 ≤ 100
# my_string과 is_suffix는 영소문자로만 이루어져 있습니다.

def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:
            return 1
    else:
        return 0

def solution2(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
# endswith() is if the end part of my_string equal to is_suffix, it will return True
# endswith()는 my_string의 끝 부분이 is_suffix와 일치하면 True를 반환
# True returns to 1, False returns to 0 , True는 1, False는 0으로 반환

print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))
print("-----------------------------")
print(solution2("banana", "ana"))
print(solution2("banana", "nan"))
print(solution2("banana", "wxyz"))
print(solution2("banana", "abanana"))