# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
# my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
# my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 
# 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항) # 1 ≤ my_string의 길이 ≤ 1,000

def solution(my_string):
    counts = [0] * 52
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            index = ord(ch) - ord('A')  # 0~25
        elif 'a' <= ch <= 'z':
            index = ord(ch) - ord('a') + 26  # 26~51
        counts[index] += 1
    return counts

print(solution("Programmers"))