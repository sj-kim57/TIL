import sys

input = sys.stdin.readline

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  arr1 = set([int(input()) for _ in range(a)])
  arr2 = set([int(input()) for _ in range(b)])
  cnt = 0
  for i in arr1:
    if i in arr2:
      cnt += 1
  print(cnt)
