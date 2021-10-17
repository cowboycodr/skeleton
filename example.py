from skeleton import Skeleton

with open('skellang.txt') as file:
  skellang = file.read()

lang = Skeleton(skellang)

vars = {}

def add_vars(string: str):
  SPLIT = lang.tokens['SPLIT']

  result = ''

  for word in string.split(SPLIT):
    if word in vars:
      result += vars[word]
    else:
      result += word
    result += ' '

  return result

@lang.keyword("`name`=`value`")
def assign(args):
  NAME = args['name']
  VALUE = args['value']

  vars[NAME] = VALUE

@lang.keyword("concat `1` `2`")
def concat(args):
  return (
    add_vars(args['1']) + add_vars(args['2'])
    )

@lang.keyword("out `message`")
def print_message(args):
  print(add_vars(args['message']))

lang.execute()