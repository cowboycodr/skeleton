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

@lang.keyword("out `message`")
def out(args):
  MESSAGE = args['message']

  print(MESSAGE)

@lang.keyword("py `code`")
def py(args):
  CODE = add_vars(args['code'])

  return eval(CODE)

@lang.keyword("eval `code`")
def evaluate(args):
  CODE = add_vars(args['code']).replace('"', '`')

  try:
    lang.evaluate(CODE)
  except:
    raise Exception("Not working!")

lang.execute()