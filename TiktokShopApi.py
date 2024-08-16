import requests

class TiktokShopApi:
  def __init__(self, x_rapidapi_key: str):
    self.x_rapidapi_key = x_rapidapi_key
    self.host = 'tiktok-shop-api.p.rapidapi.com'
    self.base_url = 'https://tiktok-shop-api.p.rapidapi.com'
    self.headers = {
      'x-rapidapi-host': self.host,
      'x-rapidapi-key': self.x_rapidapi_key
    }

  def _request(self, url: str, params=None):
    res = requests.get(url, headers=self.headers, params=params)
    res.raise_for_status()
    return res.json()
  
  def get_seller_products(
    self,
    user_id: str,
    region: str,
    count: int = 10,
    cursor: int = 0
  ):
    url = f'{self.base_url}/api/shop/product/user'
    params = {
      'uniqueId': user_id,
      'region': region,
      'count': count,
      'cursor': cursor
    }

    res = self._request(url, params)

    return res
  
  def get_product_detail(
    self,
    product_id: str,
    region: str
  ):
    url = f'{self.base_url}/api/shop/product/detail'
    params = {
      'productId': product_id,
      'region': region
    }

    res = self._request(url, params)

    return res
  
  def get_product_reviews(
    self,
    product_id: str,
    region: str,
    count: int = 10,
    cursor: int = 0,
    sort_type: int = 1 # 1: Sort by Relevance | 2: Sort by Recent
  ):
    url = f'{self.base_url}/api/shop/product/reviews'
    params = {
      'productId': product_id,
      'region': region,
      'count': count,
      'cursor': cursor,
      'sortType': sort_type
    }

    res = self._request(url, params)

    return res
  
  def search_products(
    self,
    keyword: str,
    region: str,
    count: int = 10,
    cursor: int = 0
  ):
    url = f'{self.base_url}/api/shop/search'
    params = {
      'keyword': keyword,
      'region': region,
      'count': count,
      'cursor': cursor
    }

    res = self._request(url, params)

    return res
  