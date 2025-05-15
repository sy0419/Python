# 문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 
# 크기를 return 하는 solution 함수를 완성해 주세요.
# 제한사항
# 1 ≤ strArr의 길이 ≤ 100,000
# 1 ≤ strArr의 원소의 길이 ≤ 30
# strArr의 원소들은 알파벳 소문자로 이루어진 문자열입니다.

def solution(strArr):
    lengthCount = {}
    for string in strArr:
        length = len(string)
        if length in lengthCount:
            lengthCount[length] += 1
        else:
            lengthCount[length] = 1
    max_count = max(lengthCount.values()) 
    return max_count

print(solution(["a","bc","d","efg","hi"]))