"""
1000
제목 : A+B
https://www.acmicpc.net/problem/1000

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.

예제 입력 1
1 2
예제 출력 1
3


"""

sum = 0
for n in map(int, input().split()):
    sum += n
print(sum)

from sys import stdin
sum = 0
for n in map(int, stdin.read().split()):
    sum += n
print(sum)