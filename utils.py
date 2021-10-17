def unpack_dictionary(dictionary):
  for key in dictionary:
    yield (key, dictionary[key])
  
def only(character: str, string: str):
  # returns true if string only contains the character given

  if string.count(character) == len(string):
    return True
  else: return False