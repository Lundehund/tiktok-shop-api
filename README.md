# Tiktok Shop API Python (Unofficial)

<p align="center">
  <img src="https://github.com/Lundehund/tiktok-shop-api/blob/main/public/tiktok-shop-png.png" width="400">
</p>

[![GitHub Repo stars](https://img.shields.io/github/stars/Lundehund/tiktok-shop-api?style=social)](https://github.com/Lundehund/tiktok-shop-api/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/Lundehund/tiktok-shop-api?style=social)](https://github.com/Lundehund/tiktok-shop-api/network/)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https://twitter.com)](https://twitter.com)
[![Vistors](https://visitor-badge.laobi.icu/badge?page_id=Lundehund.tiktok-shop-api&title=Visitors)](https://github.com/Lundehund/tiktok-shop-api)
[![License](https://img.shields.io/github/license/Lundehund/tiktok-shop-api?label=License)](https://mit-license.org/)

## Getting Started

Import the `TiktokShopApi` class and add your RapidAPI Key. You can get the key at [RapidAPI Tiktok Shop](https://rapidapi.com/Lundehund/api/tiktok-shop-api).

```python
from TiktokShopApi import TiktokShopApi

x_rapidapi_key = 'YOUR_X_RAPIDAPI_KEY'
client = TiktokShopApi(x_rapidapi_key)
```



## Methods
- get_seller_products(user_id, region, count, cursor)
- get_product_detail(product_id, region)
- get_product_reviews(product_id, region, count, cursor, sort_type)
- search_products(keyword, region, count, cursor)

## Examples

The file `/example.py` is an example of searching for products (with keyword `labubu` and region `TH`) on TikTok Shop and saving valuable data to a CSV file.

You can view this file in `labubu.csv` or try with your own keyword.

![Example-search-labub](./public/example-csv.png)

Alternatively, you can go to the `/examples` folder to view the raw results in JSON format.
