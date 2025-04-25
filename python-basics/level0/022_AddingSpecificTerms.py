# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 
# 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.
# 제한사항)
# 1 ≤ a ≤ 100
# 1 ≤ d ≤ 100
# 1 ≤ included의 길이 ≤ 100
# included에는 true가 적어도 하나 존재합니다.

def solution(a, d, included):
    total = 0
    for i in range(len(included)):
        if included[i]:
            total += a + d * i
    return total

print(solution(3, 2, [True, False, False, True, True])) #23
print(solution(3, 4, [True, False, False, True, True])) #27
print(solution(7, 1, [False, False, False, True, False, False, False])) #10