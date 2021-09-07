import  requests

response = requests.get ('https://check2001.herokuapp.com/')

print(response)
print(response.url)