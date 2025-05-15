# 정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. 
# arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
# 제한사항)  1 ≤ arr의 길이 ≤ 1,000 , 1 ≤ arr의 원소 ≤ 1,000

def solution(arr):
    n = 0
    while 2 ** n < len(arr):
        n += 1
    target_length = 2 ** n
    add_zeros = target_length - len(arr)
    return arr + [0] * add_zeros

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))