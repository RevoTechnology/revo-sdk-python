from revo_api import RevoAPI
from revo_api import RevoAPIConfig

config = RevoAPIConfig(
  callback_url="http://example.com/callback",
  redirect_url="http://example.com/redirect",
  store_id="93",
  secret="4c97e12e1f37ff3006d552134543a3a7651b9743",
  test_mode=True
)

revo = RevoAPI(config)

# order form iframe link

print revo.order_iframe_link('ORDER_423', 99.99)
print revo.order_iframe_link('ORDER_424', 249.99, {'primary_phone': '9876543021', 'primary_email': 'mail@example.com'})

# preorder form iframe link

print revo.preorder_iframe_link()
print revo.preorder_iframe_link('9014536782')


# limit by phone

print revo.limit_by_phone('912345678')

# partial order return

print revo.return_order('ORDER_211', 19.25)

