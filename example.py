from skeleton import Skeleton

skellang = """
log $Welcome_to_Skellang!
"""

langauge = Skeleton(skellang)

def log(args): 
  MESSAGE = args['message']
  print(MESSAGE.replace('_', ' '))

langauge.add_action(
  'log $message',
  log
)

langauge.execute()