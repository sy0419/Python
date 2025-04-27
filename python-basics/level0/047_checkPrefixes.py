# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# 1 ≤ is_prefix의 길이 ≤ 100
# my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

def solution(my_string, is_prefix):
    for i in range(len(my_string)):
        if my_string[:i] == is_prefix:
            return 1
    return 0

def solution2(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
# endswith() is if the start part of my_string equal to is_prefix, it will return True
# endswith()는 my_string의 시작 부분이 is_prefix와 일치하면 True를 반환
# True returns to 1, False returns to 0 , True는 1, False는 0으로 반환

print(solution("banana", "ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))
print("-----------------------------")
print(solution2("banana", "ban"))
print(solution2("banana", "nan"))
print(solution2("banana", "abcd"))
print(solution2("banana", "bananan"))