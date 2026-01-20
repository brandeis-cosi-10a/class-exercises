import format
from spellcheck import RandomSpellChecker

text = input("Type something: ")

sc = RandomSpellChecker(0.25)
if sc.check(text):
  print("Great spelling!")
  print(format.make_excited(text))
else:
  print("Looks like you have some spelling errors...")
  print(format.make_sad(text))