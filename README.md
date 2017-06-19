# RevoSDK Python Library

Python Library to access Revo API

## Basic usage

Revo API implements four methods:

* check client's limit by phone number (`limit_by_phone` method)
* getting form link for preorder (`preorder_iframe_link` method)
* getting form link for full order process (`order_iframe_link` method)
* performing partial of full order return ((`return order` method)

API client must be configured as follows:

```python
from revo_api import RevoAPI
from revo_api import RevoAPIConfig

config = RevoAPIConfig(
	callback_url="http://example.com/callback",
	redirect_url="http://example.com/redirect",
	store_id="12",
	secret="3d657e24e1f37aa3006d552134543a3a7651b9743",
	test_mode=True
)

revo = RevoAPI(config)

```

* `test_mode` indicates whether production or demo mode to use (by default set `true`)
* `redirect_url` must be URL to which user will be redirected after form submit
* `callback_url` must be URL to which Revo will send callback data
* `store_id` - store id in Revo system
* `secret` - hash-like string for creating signature from Revo (must be stored privately)

After setting up `RevoAPIConfig` you may access API methods in `RevoAPI`.

### Example

```python
# init with config before
revo = RevoAPI(config)

# basic order form iframe link method
order_iframe = revo.order_iframe_link('ORDER_423', 99.99)

# preorder form iframe link method with prepopulated "phone" field
preorder_iframe = revo.preorder_iframe_link('9014536782')

# checking limit by phone
revo.limit_by_phone('912345678')
```

See also the [examples.py](examples.py) file.


## Contributing ##

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


Since here in RevoTechnologies we try to provide any developer with proper instruments, we greatly appreciate your help in improving this or any other language SDK :)

