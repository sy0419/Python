# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)^2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
# 제한사항) a, b, c, d는 1 이상 6 이하의 정수입니다.

def solution(a, b, c, d):
    result = 0
    dice = [a, b, c, d]
    dupli_cnt = list(set(dice))  # The list which removes duplication , 중복을 제거한 리스트

    
    if len(dupli_cnt) == 1: # When the dice have all same numbers , 모든 주사위 수가 같은 경우
        result = 1111 * dice[0]
        
    elif len(dupli_cnt) == 2: # When dice have two different kind of numbers , 주사위 숫자가 2 종류인 경우
        p, q = dupli_cnt
        p_cnt = dice.count(p)  # Count of p , p의 개수
        q_cnt = dice.count(q)  # Count of q , q의 개수
        if p_cnt == 3: # When 3 dices have same numbers ans 1 dice has different number , 같은 숫자가 (3개, 1개) 나오는 경우
            result = (10 * p + q) ** 2
        elif q_cnt == 3: # When 1 dice has different number and 3 dices have same number , 같은 숫자가 (1개, 3개) 나오는 경우
            result = (10 * q + p) ** 2
        else: # When each 2 dices have same numbers , 같은 숫자가 (2개, 2개) 나오는 경우
            result = (p + q) * abs(p - q)
        
    elif len(dupli_cnt) == 3: # When dice have three different kind of numbers , 주사위 숫자가 3 종류인 경우
        for num in dupli_cnt:
            if dice.count(num) == 2: # Find the number which two dice have , 2개가 같은 숫자 찾기
                p = num
                break
                
        q_r_list = [] # Find the number which each of dice have , 나머지 1개씩 나온 숫자 2개 추출
        for x in dupli_cnt:
            if x != p:
                q_r_list.append(x)
        q, r = q_r_list[0], q_r_list[1]
        result = q * r
        
    elif len(dupli_cnt) == 4: # When dice have all different numbers , 모든 주사위가 다 다른 수인 경우
        result = min(dice) # Mininum value , 가장 작은 값
        
    return result

print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))