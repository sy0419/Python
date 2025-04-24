# 문제 설명
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
# 1 ≤ str1의 길이 = str2의 길이 ≤ 10
# str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.

def solution(str1, str2):
    answer = ''
    for string in range(len(str2)): # Loop over the length of str2
                                    # str2의 길이만큼 반복한다.
        answer += str1[string] + str2[string]
    return answer

str1 = "aaaaa"
str2 = "bbbbb" 
result = solution(str1, str2)
print(result)