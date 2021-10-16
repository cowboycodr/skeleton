# Skeleton langauge framework

import re

from utils import unpack_dictionary

class Skeleton:
  def __init__(self, langauge):
    self.language = langauge

    # The vocab of programming languages
    self.tokens = {
      'SPLIT': ' ',
      'TERMINATOR': ';',
      'WORD': r'([^\s]*)',
      'PARAM': r'`([^`]*)`'
    }

    self.garbage_tokens = ['/']

    self.replacements = {
      "_": " "
    }

    self.__actions = {}

  def __validate_keyword(self, action: str):
    # Validates the action and tell whether its necessary

    for token in self.garbage_tokens:
      if action.startswith(token):
        raise Exception(f'Statement: "{action}": conflicts with garbage token: {token}')

  def get_queries(self, string: str):
    PARAM = self.tokens['PARAM']

    queries = re.findall(f'{PARAM}', string, re.MULTILINE)

    return queries

  def clean(self, string: str):
    # Cleans parsable string
    # 
    # Returns cleaned string, and keyword (optional)

    SPLIT = self.tokens['SPLIT']

    result = ''

    string = string.strip('\r\n')

    for word in string.split(SPLIT):
      if word not in self.garbage_tokens:
        result += word + SPLIT

    return result

  def add_keyword(self, statement: str, action):
    self.__validate_keyword(statement)

    # TOKENS
    SPLIT = self.tokens['SPLIT']
    WORD = self.tokens['WORD']
    PARAM = self.tokens['PARAM']
    PARAM_REGEX = re.compile(PARAM)

    statement = self.clean(statement)

    pattern_string = r'(\W*)'

    for word in statement.split(SPLIT)[:-1]:
      if PARAM_REGEX.match(word):
        pattern_string += (PARAM + SPLIT)
      else:
        pattern_string += (word + SPLIT)

    pattern_string = pattern_string[:-1] + r'(\W*)'
    args = self.get_queries(statement)

    self.__actions[statement] = {
      'func': action,
      'args': args,
      'pattern': pattern_string
    }

  def keyword(self, statement: str):
    def decorator(function):
      self.add_keyword(statement=statement, action=function)
    return decorator

  def execute(self):
    TERMINATOR = self.tokens['TERMINATOR']

    self.language = self.clean(self.language)

    for statement in self.language.split(TERMINATOR):
      # statement = statement.strip().replace('\n', '').replace(r'\n', ' ')
      executed = False
      for (action_statement, action) in unpack_dictionary(self.__actions):
        action_pattern = re.compile(action['pattern'], flags=re.MULTILINE)

        if action_pattern.match(statement.replace('\n', '')):
          statement_queries = self.get_queries(statement)

          action_args = action['args']
          statement_args = {}

          for arg in range(0, len(action_args)):
            statement_args[action_args[arg]] = statement_queries[arg]

          action['func'](statement_args)
          executed = True
      if not executed and not len(statement) < 2 and statement[0] not in self.garbage_tokens:
         raise Exception(f'"{statement}" is not a valid statement')