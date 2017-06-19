class RevoAPIException(Exception):
  def __init__(self, code, message):
    self.value = 'Error ' + str(code) + ': ' + message

  def __str__(self):
    return repr(self.value)
