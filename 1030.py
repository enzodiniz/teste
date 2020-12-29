nc = int(input())

for vezes in range(nc):
  n, k = [int (i) for i in input().split()]
  pessoas = []

  for i in range(n):
    pessoas.append(i+1)

  index = -1;
  while len(pessoas) > 1:
    index = index + k

    while index >= len(pessoas):
      index = index - len(pessoas)

    pessoas.pop(index)
    index = index - 1

  print(f'Case {vezes+1!s}: { pessoas[0]!s} ')