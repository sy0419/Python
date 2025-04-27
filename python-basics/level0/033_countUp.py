# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# 제한사항) 0 ≤ start_num ≤ end_num ≤ 50

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

def solution2(start_num, end_num):
    return list(range(start_num, end_num+1))

print(solution(3, 10))
print(solution2(3, 10))