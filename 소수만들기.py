#프로그래머스 1: 소수만들기
from itertools import combinations

def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def solution(nums):
    answer = 0
    lst = list(combinations(nums, 3))

    for n in lst:
        num = sum(n)
        if is_prime_number(num):
            answer += 1

    return answer