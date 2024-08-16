import csv
from TiktokShopApi import TiktokShopApi

# Get your key at: https://rapidapi.com/Lundehund/api/tiktok-shop-api
x_rapidapi_key = 'YOUR_X_RAPIDAPI_KEY'
if not x_rapidapi_key or x_rapidapi_key == 'YOUR_X_RAPIDAPI_KEY':
  raise Exception('x_rapidapi_key is required')

client = TiktokShopApi(x_rapidapi_key)

keyword = 'labubu'
region = 'TH'
count = 10
cursor = 0

max_num = 50
results = []

with open(f'{keyword}.csv', 'w', newline='') as file:
  headers = [
    'id', 'title', 'cover', 'currency', 'price',
    'sold_count', 'discount', 'rating', 'review_count',
    'seller_name', 'seller_id', 'seller_tiktok_id'
  ]
  writer = csv.DictWriter(file, fieldnames=headers)
  writer.writeheader()
  
  while len(results) <= max_num:
    res = client.search_products(keyword, region, count, cursor) or {}
    products = res.get('products')
    has_more = res.get('has_more')
    cursor = res.get('cursor')

    if len(products) == 0:
      break

    for product in products:
      info = product.get('product_info') or {}
      seller = info.get('seller_product_info') or {}
      
      print(f'Product {info.get("product_id")}')
      product_extracted = {
        'id': info.get('product_id'),
        'title': info.get('title'),
        'cover': info.get('cover'),
        'currency': info.get('currency'),
        'price': info.get('format_price'),
        'sold_count': info.get('sold_count'),
        'discount': info.get('format_discount'),
        'rating': info.get('product_rating'),
        'review_count': info.get('review_count'),
        'seller_name': seller.get('seller_name'),
        'seller_id': seller.get('seller_id'),
        'seller_tiktok_id': seller.get('shop_creator_info', {}).get('user_id')
      }
      results.append(product_extracted)
      writer.writerow(product_extracted)

    if has_more == False:
      break