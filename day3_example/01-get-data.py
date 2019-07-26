import json, requests

url = "https://api.exchangeratesapi.io/history?start_at=2019-05-06&end_at=2019-05-19&base=IDR&symbols=CNY,USD"

response = requests.get(url)
data = response.text
parsed = json.loads(data)

print(json.dumps(parsed, indent=2))
