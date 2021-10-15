# Rapidly creating a programming language with Skeleton framework!
from skeleton import Skeleton

with open('skellang.txt') as file:
  skellang = file.read()

lang = Skeleton(skellang)

@lang.action('out `message`')
def out(args):
  print(args['message'])

@lang.action('py `code`')
def py(args):
  exec(args['code'])

@lang.action('timeout `time`')
def timeout(args):
  import time as t

  t.sleep(float(args['time']))

lang.execute()