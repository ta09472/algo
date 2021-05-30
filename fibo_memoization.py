memoization = [0] * 100 # 한 번 계산된 결과를 메모아제이션하기 위한 리스트 초기화
def fibo(x):
    if x == 0 or x == 1: # 종료조건
        return 1

    if memoization[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
        return memoization[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    memoization[x] = fibo(x-1) + fibo(x-2)
    return memoization[x]

print(fibo(99))
