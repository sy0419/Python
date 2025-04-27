# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항
# 1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
# 1 ≤ my_strings의 원소의 길이 ≤ 100
# parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
# 0 ≤ s ≤ e < my_strings[i]의 길이

def solution(my_string, parts):
    answer = ''
    for string, part in zip(my_string, parts): #zip makes two different list to run at the same time , zip은 두 리스트를 동시에 묶어서 반복할 수 있도록 한다.
        s, e = part
        answer += string[s:e+1]
    return answer

def solution2(my_strings, parts):
    answer = ""
    for i in range(len(my_strings)):
        string = my_strings[i]
        s, e = parts[i]
        sub_str = string[s:e+1]
        answer += sub_str
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))
print(solution2(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))