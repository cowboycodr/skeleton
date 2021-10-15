from skeleton import Skeleton

# Reading from file
with open('skellang.txt') as file:
  skellang = file.read()

lang = Skeleton(skellang)

@lang.action("out `message`")
def out(args):
  print(args['message'])

@lang.action("loop `times` `message`")
def loop(args):
  for _ in range(int(args['times'])):
    print(args['message'])

lang.execute()