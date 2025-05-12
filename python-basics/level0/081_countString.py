# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
# 제한사항) 1 ≤ myString ≤ 1000 , 1 ≤ pat ≤ 10

def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            answer += 1
    return answer

print(solution("banana", "ana"))
print(solution("aaaa", "aa"))