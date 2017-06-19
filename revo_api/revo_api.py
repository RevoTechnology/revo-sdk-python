from utils import Utils

class RevoAPI:
  def __init__(self, config):
    self.api = Utils(config)

  def order_iframe_link(self, order_id, amount, additional_params = {}):
    order_data = self.api.order_data(order_id, amount, additional_params)
    response = self.api.call_service(order_data, 'order')
    return self.api.parse_order(response)

  def preorder_iframe_link(self, phone = ''):
    additional_params = {}
    if phone: additional_params.update({'primary_phone': phone})

    order_data = self.api.order_data(self.api.random_order_id(), 1.0, additional_params)
    response = self.api.call_service(order_data, 'order')
    return self.api.parse_order(response)

  def limit_by_phone(self, phone):
    limit_data = self.api.limit_data(phone)
    response = self.api.call_service(limit_data, 'phone')
    return self.api.parse_limit(response)

  def return_order(self, order_id, amount):
    return_data = self.api.return_data(order_id, amount)
    response = self.api.call_service(return_data, 'return')
    return self.api.parse_return(response)


