"""
The file to test the login mechanism of the webiste 
"""

import requests

login_url = "http://localhost:5000/pgsql/login"

signup_url = "http://localhost:5000/pgsql/signup"

update_url = "http://localhost:5000/pgsql/update"

recover_url = "http://localhost:5000/pgsql/recover"

delete_url = "http://localhost:5000/pgsql/delete"


data_login = {"username": "abhi2" ,"password" : "1234"}
data_signup = {"username": "abhi4" ,"password" : "Qwerty@8503001887" , "confirm_password": "Qwerty@8503001887" }
data_update = {"username": "abhi2" ,"old_password" : "Qwerty@1235" , "new_password": "1234" , "confirm_password" : "1234"}
data_recover = {"username": "abhi4" ,"token" : "hjs&99" , "new_password": "1235" , "confirm_password" : "1235"}
data_delete =  {"username": "abhi4" ,"token" : "hjs&99" , "password": "1235" }




response_login = requests.post(login_url, json=data_login)
response_signup = requests.post(signup_url ,json = data_signup)
response_update = requests.put(update_url , json = data_update)
response_recover = requests.put(recover_url , json = data_recover )
response_delete = requests.delete(delete_url , json = data_delete)






print(response_login.status_code)
print(response_login.json()) 


print(response_signup.status_code)
print(response_signup.json())


print(response_update.status_code)
print(response_update.json())

print(response_recover.status_code)
print(response_recover.json())


print(response_delete.status_code)
print(response_delete.json())