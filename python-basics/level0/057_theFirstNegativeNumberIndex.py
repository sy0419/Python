# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 
# 음수가 없다면 -1을 return합니다.
# 제한사항)  5 ≤ num_list의 길이 ≤ 100 , -10 ≤ num_list의 원소 ≤ 100

def solution(num_list):
    answer = -1
    for i, num in enumerate(num_list):
        if num < 0:
            answer = i
    return answer

print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))