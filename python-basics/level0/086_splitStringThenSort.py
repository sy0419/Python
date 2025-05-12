# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 
# 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, 빈 문자열은 반환할 배열에 넣지 않습니다.
# 제한사항) 1 ≤ myString ≤ 100,000 , myString은 알파벳 소문자로 이루어진 문자열입니다.

def solution(myString):
    answer = []
    splitStr = myString.split("x")
    splitStr = list(filter(None, splitStr))  # empty string removing 빈 문자열 제거
    splitStr.sort()
    for string in splitStr:
        answer.append(string)
    return answer

print(solution("axbxcxdx"))
print(solution("dxccxbbbxaaaa"))