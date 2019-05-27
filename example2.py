# example2.py

string = "HolaMundoCaraCulo"

def count_mayus(string):
  up = string.upper()
  n_mayus = 0
  for i in range(len(string)):
    if string[i] == up[i]:
      n_mayus  += 1

  return n_mayus


print(count_mayus(string))
