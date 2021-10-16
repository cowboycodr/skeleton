from skeleton import Skeleton

with open('skellang.txt') as file:
  skellang = file.read()

lang = Skeleton(skellang)

vars = {}

def add_vars(string):
  for key in vars:
    string = string.replace(key, vars[key])

  return string

@lang.keyword('concat `string` and `string1`')
def concat(args):
  print(args['string'] + args['string1'])

lang.execute()