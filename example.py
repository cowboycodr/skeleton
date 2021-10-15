# import skeleton langauge-framework
from skeleton import Skeleton

# read content from file 
with open('skellang.txt') as file:
  skellang_content = file.read()

# create langauge 
lang = Skeleton(skellang_content)

# add langauge keyword
@lang.action(statement="out `message`")
def out(args):
  print(
    args['message']
  )


# execute created langauge
lang.execute()