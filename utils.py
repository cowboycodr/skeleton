def unpack_dictionary(dictionary):
  for key in dictionary:
    yield (key, dictionary[key])
  
