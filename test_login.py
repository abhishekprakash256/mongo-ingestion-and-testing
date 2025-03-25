"""
The file to test the login mechanism of the webiste 
"""

import requests

login_url = "http://localhost:5000/pgsql/login"


data = {"username": "abhi2" ,"password" : "Qwerty@1235"}

response = requests.post(login_url, json=data)

print(response.status_code)
print(response.json()) 