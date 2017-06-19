import json
import hashlib
import httplib, urllib
import time
import random
from error import RevoAPIException

class Utils:
  def __init__(self, config):
    self.config = config

  def order_data(self, order_id, amount, additional_params):
    payload = {
      'callback_url': self.config.callback_url,
      'redirect_url': self.config.redirect_url,
      'current_order': {
        'sum': "%.2f" % amount,
        'order_id': order_id
      }
    }

    payload.update(additional_params)
    return json.dumps(payload)

  def limit_data(self, phone):
    payload = {'client': {'mobile_phone': phone}}
    return json.dumps(payload)

  def return_data(self, order_id, amount):
    payload = {'order_id': order_id, 'sum': "%.2f" % amount, 'kind': 'cancel'}
    return json.dumps(payload)

  def call_service(self, data, type):
    signature = self.__sign(data)
    query = {'store_id': self.config.store_id, 'signature': signature}
    url = self.__build_url(query, type)

    conn = httplib.HTTPSConnection(self.config.base_host)
    conn.request("POST", url, data)
    response = conn.getresponse()

    if response.status is 200:
      data = response.read()
      return data
    else:
      raise RevoAPIException(response.status, response.reason)

  def parse_order(self, data):
    response = json.loads(data)
    if response['status'] != 0:
      raise RevoAPIException(response['status'], response['message'])
    else:
      return response['iframe_url']

  def parse_limit(self, data):
    response = json.loads(data)
    if response['meta']['status'] != 0:
      raise RevoAPIException(response['meta']['status'], response['meta']['message'])
    else:
      return response['client']

  def parse_return(self, data):
    response = json.loads(data)
    if response['status'] != 0:
      raise RevoAPIException(response['status'], response['message'])
    else:
      return {'status': 'ok'}

  def random_order_id(self):
    order_id = 'ORDER_'
    order_id += str(random.randint(100000, 1000000))
    order_id += '_'
    order_id += str(int(time.time()))
    return order_id

  def __sign(self, data):
    return hashlib.sha1(data + self.config.secret).hexdigest()

  def __build_url(self, query, type):
    endpoints = {
      'return': '/online/v1/return',
      'phone': '/api/external/v1/client/limit',
      'preorder': '/iframe/v1/auth',
      'order': '/iframe/v1/auth'
    }

    return endpoints[type] + '?' + urllib.urlencode(query)
