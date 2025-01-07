from random import uniform

class RandomSpellChecker:
  '''
  A "spell checker" that randomly decides if spelling in text is correct.
  '''

  def __init__(self, success_chance):
    self.success_chance = success_chance

  def check(self, text):
    choice = uniform(0, 1)
    if choice < self.success_chance:
      return True
    return False