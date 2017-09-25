import requests

headers = {
    'Authorization': 'Basic Q0EyMGc2RnRNRE1xMlZ6Y3hnTHBMR0o1b1RjYTpDbzlUYTRUcUZGQldRMmNQT2phZjFKV0R2RUlh',
}

data = [
  ('grant_type', 'password'),
  ('username', '<USER>'),     #@@ Must change
  ('password', '<PASSWORD>'), #@@ Must change
]
  
token = requests.post('https://api.vasttrafik.se:443/token', headers=headers, data=data, verify=False)
token.text

#token should be <Response [200]>
# example of token.text : '{"token_type":"Bearer","expires_in":3600,
#"refresh_token":"7e71450c-2f01-333a-b22f-0642f40f875d",
#"access_token":"8682918a-5bdf-33fc-ab45-2a85dc6b54c8"}'
