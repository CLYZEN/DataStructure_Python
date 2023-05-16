# 속도를 측정하고자 하는 알고리즘
def find_max(A):
    max = A[0]
    for item in A:
        if item > max:
            max = item
    return max


# 실행시간 측정 프로그램
import time  # time 모듈 import

array = [1, 4, 8, 12, 15, 3, 55, 23]

start = time.time()  # 현재 시각을 저장
max = find_max(array)  # 시간을 측정하려는 코드
end = time.time()  # 현재 시각을 저장

print("최댓값 = ", max)
print("실행시간 = ", end - start)  # 실행 시간(종료-시작)을 출력

print("-------------------------")
# array 의 크기를 10000개의 난수(0~10000)로 선언하여 실행 시간 늘리기
import random  # random 모듈 import

array = [random.randint(0, 10000) for i in range(10000)]

start = time.time()  # 현재 시각을 저장
for n in range(10000):
    max = find_max(array)
end = time.time()  # 현재 시각을 저장

print("최댓값 = ", max)
print("실행시간 = ", end - start)  # 실행 시간(종료-시작)을 출력
