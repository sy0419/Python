# 정수가 담긴 리스트 num_list가 주어집니다. 
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9
# num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.

def solution(num_list):
    oddnum = "" 
    evennum = ""
    for number in num_list:
        if number % 2 == 1:
            oddnum += str(number)
        else:
            evennum += str(number)
    answer = int(oddnum) + int(evennum)
    return answer


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))