class Node:

  def __init__(self, value):
    self.value = value
    self.proximo = None

  def setProximo(self, proximo):
    self.proximo = proximo

  def getProximo(self):
    return self.proximo

class List:
  first = None
  last = None
  size = 0

  def add(self, value):
    if self.first is None:
      self.first = Node(value)
      self.last = self.first
      self.size = 1
    else :
      self.last.setProximo(Node(value))
      self.last = self.last.getProximo()
      self.size = self.size + 1

  def kill(self, pulo, nodeInicial):
    # nodeZero = Node(-1)
    # nodeZero.setProximo(self.first)

    # current = nodeZero
    current = nodeInicial

    if pulo > self.size:
      pulo = pulo % self.size

    for i in range(pulo-1):
      current = current.getProximo()

    # print('to remove: ', current.getProximo().value)

    if current.getProximo() == self.first:
      self.first = self.first.getProximo()

    if current.getProximo() == self.last:
      self.last = current

    current.setProximo(current.getProximo().getProximo())

    return current

  def printAll(self):
    current = self.first
    while current != self.last:
      print(str(current.value) + ' -> ' + str(current.getProximo().value))
      current = current.getProximo()
    print(str(current.value) + ' -> ' + str(current.getProximo().value))

nc = int(input())

for vezes in range(nc):
  numeroPessoas, k = [int (i) for i in input().split()]

  pessoas = List()
  for i in range(numeroPessoas):
    pessoas.add(i+1)

  pessoas.last.setProximo(pessoas.first)
  # print('last:', pessoas.last.value)
  # print('last proximo:', pessoas.last.getProximo().value)

  # pessoas.printAll()

  print('size: ', pessoas.size)

  nodeZero = Node(-1)
  nodeZero.setProximo(pessoas.first)

  current = pessoas.kill(k, nodeZero)

  while pessoas.first != pessoas.last:
    current = pessoas.kill(k, current)

  print(f'Case {vezes+1!s}: { pessoas.first.value!s} ')
  
