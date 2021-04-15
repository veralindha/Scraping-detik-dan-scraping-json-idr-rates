import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8555526392209e-5,"date":"Thu, 15 Apr 2021 00:00:01 GMT","inverseRate":14586.716091697},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.729035883124e-5,"date":"Thu, 15 Apr 2021 00:00:01 GMT","inverseRate":17454.943910296}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

