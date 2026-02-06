## monty_hall

'''
I could understand the explanation of the Monty Hall problem
but needed some more evidence

References:
  http://www.bbc.co.uk/dna/h2g2/A1054306
  http://en.wikipedia.org/wiki/Monty_Hall_problem especially:
  http://en.wikipedia.org/wiki/Monty_Hall_problem#Increasing_the_number_of_doors
'''
from random import randrange

doors, iterations = 3,100000  # could try 100,1000


def monty_hall(choice, switch=False, doorCount=doors):
  # Set up doors
  door = [False]*doorCount
  # One door with prize
  door[randrange(doorCount)] = True

  chosen = door[choice]

  unpicked = door
  del unpicked[choice]

  # Out of those unpicked, the alternative is either:
  #   the prize door, or
  #   an empty door if the initial choice is actually the prize.
  alternative = True in unpicked

  if switch:
    return alternative
  else:
    return chosen
