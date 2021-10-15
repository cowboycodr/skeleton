from skeleton import Skeleton

import js2py

with open('skellang.txt') as file:
  skellang = file.read()

langauge = Skeleton(skellang)

@langauge.action("log $message")
def log(args):
  MESSAGE = args["message"].replace('_', ' ')

  print(MESSAGE)

@langauge.action("py $code")
def exe(args):
  eval(args["code"].replace('_', ' '))

@langauge.action("js $code")
def js(args):
  print(js2py.eval_js(args['code'].replace('_', ' ')))

langauge.tokens["TERMINATOR"] = "\n"
langauge.execute()