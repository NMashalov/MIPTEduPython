import requests

URL = 'http://127.0.0.1:8000'

r = requests.post(URL + '/create_user/',params={
    'name': 'Vladislav'
})

print(r.status_code)
print(r.text)

r = requests.get(URL + '/select_user/')

print(r.status_code)
print(r.text)

r = requests.get(URL + '/divide_zero/')

print(r.status_code)
print(r.text)