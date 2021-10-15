from skeleton import Skeleton

skellang = """
log $Welcome_to_Skellang!
"""

langauge = Skeleton(skellang)

@langauge.action(statement="log $message")
def log(args):
  MESSAGE = args['message'].replace('_', ' ')

  print(MESSAGE)

langauge.execute()