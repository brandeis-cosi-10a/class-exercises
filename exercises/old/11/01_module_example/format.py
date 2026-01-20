def make_excited(text):
  '''
  Make `text` more excited by replacing '.' with '!', and returning the new string.
  '''
  return text.replace('.', '!')


def make_sad(text):
  '''
  Make `text` more sad by adding a ':(' to the end and returning the new string.
  '''
  return text + " :("