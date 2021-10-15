# Skeleton langauge framework

import re
from functools import wraps

from utils import unpack_dictionary

class Skeleton:
  def __init__(self, langauge):
    self.language = langauge

    # The vocab of programming languages
    self.tokens = {
      'SPLIT': ' ',
      'TERMINATOR': ';',
    }

    self.garbage_tokens = ['#']

    self.__actions = {}

  def __get_statement_keyword(self, statement):
    return statement.split(self.tokens['SPLIT'])[0]

  def __validate_action(self, action: str):
    # Validates the action and tell whether its necessary

    for token in self.garbage_tokens:
      if action.startswith(token):
        raise Exception(f'Statement: "{action}": conflicts with garbage token: {token}')

  def get_queries(self, string: str):
    queries = re.findall(r'\$(\S*)', string)

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

  def add_action(self, statement: str, action,  strict: bool = False):
    # TODO: Convert to decorator

    self.__validate_action(statement)

    # TOKENS
    SPLIT = self.tokens['SPLIT']

    # Cleans the language
    if not strict:
      statement = self.clean(statement)

    keyword = self.__get_statement_keyword(statement)

    args = self.get_queries(statement)
    pattern_string = keyword + ''.join([f'{SPLIT}\$(\S*)'  for arg in args])
    # pattern = re.compile(pattern_string)

    self.__actions[statement] = {
      'func': action,
      'args': args,
      'pattern': pattern_string,
      'keyword': keyword
    }

  def action(self, statement: str, strict: bool = False):
    def decorator(function):
      self.add_action(statement=statement, action=function, strict=strict)
    return decorator

  def execute(self):
    TERMINATOR = self.tokens['TERMINATOR']

    self.language = self.clean(self.language)

    for statement in self.language.split(TERMINATOR):
      statement = statement.strip()
      for (action_statement, action) in unpack_dictionary(self.__actions):

        if re.compile(action['pattern']).match(statement):
          statement_queries = self.get_queries(statement)

          action_args = action['args']
          statement_args = {}

          for arg in range(0, len(action_args)):
            statement_args[action_args[arg]] = statement_queries[arg]

          action['func'](statement_args)