from error import RevoAPIException

class RevoAPIConfig:
  def __init__(self, callback_url, redirect_url, store_id, secret, test_mode = False):
    self.base_host = 'r.revoplus.ru'

    if test_mode: self.base_host = 'demo.revoplus.ru'

    if callback_url:
      self.callback_url = callback_url
    else:
      raise RevoAPIException(0, 'Invalid config param callback_url')

    if redirect_url:
      self.redirect_url = redirect_url
    else:
      raise RevoAPIException(0, 'Invalid config param redirect_url')

    if store_id:
      self.store_id = str(store_id)
    else:
      raise RevoAPIException(0, 'Invalid config param store_id')

    if secret:
      self.secret = secret
    else:
      raise RevoAPIException(0, 'Invalid config param secret')


