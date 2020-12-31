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

  def add(self, value):
    if self.first is None:
      self.first = Node(value)
      self.last = self.first
    else :
      self.last.setProximo(Node(value))
      self.last = self.last.getProximo()

  def kill(self, pulo, nodeInicial):
    # nodeZero = Node(-1)
    # nodeZero.setProximo(self.first)

    # current = nodeZero
    current = nodeInicial
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

  lista = List()
  for i in range(numeroPessoas):
    lista.add(i+1)

  lista.last.setProximo(lista.first)
  # print('last:', lista.last.value)
  # print('last proximo:', lista.last.getProximo().value)

  # lista.printAll()

  nodeZero = Node(-1)
  nodeZero.setProximo(lista.first)

  current = lista.kill(k, nodeZero)

  while lista.first != lista.last:
    current = lista.kill(k, current)

  print(f'Case {vezes+1!s}: { lista.first.value!s} ')


  # lista.printAll()

  # index = -1;
  # while len(pessoas) > 1:
  #   index = index + k

  #   while index >= len(pessoas):
  #     index = index - len(pessoas)

  #   pessoas.pop(index)
  #   index = index - 1

  # print(f'Case {vezes+1!s}: { pessoas[0]!s} ')