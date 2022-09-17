class js_list:
  def __init__(self, custom_list: list) -> None:
    self.is_js_list = True
    self.custom_list = custom_list
  
  def for_each(self, callback):
    print(type(callback))
    index = 0
    for element in self.custom_list:
      callback(element, index)
      index += 1


names = js_list(['Celia', 'Queipe', 'Lelso', 'Fezio'])
word = ''

def inc_first_char(string: str, index: int):
  word += string[0]
  word += str(index)

def run_for_each(word):
  names.for_each(inc_first_char)
  return word # == 'C0Q1L2F3'

print(run_for_each())
