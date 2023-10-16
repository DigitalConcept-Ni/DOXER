import json

import stripe
from keys import key

stripe.api_key = key['secret']

idProduct = stripe.Product.create(name='IN 200 BASICO + 2IC + 4', description='Segunda prueba desde python')
price = stripe.Price.create(
  unit_amount=2000,
  currency="usd",
  recurring={"interval": "day"},
  product=idProduct['id'],
)
print(price)

# p = stripe.Product.list(limit=3)
# p = stripe.Price.list(limit=3)
# print(p.data[0]['currency'])
# print(json.loads(p.data.json))