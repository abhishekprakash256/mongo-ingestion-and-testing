"""
The file to test the login mechanis m of the webiste 
"""

import requests


signup_url = "http://127.0.0.1:5001/auth/signup"

login_url = "http://127.0.0.1:5001/auth/login"

update_url = "http://127.0.0.1:5001/auth/update-password"


#recover_url = "http://127.0.0.1:5000/pgsql/recover"

delete_url = "http://127.0.0.1:5001/auth/delete"


"""

create_user_url = "http://127.0.0.1:5000/pgsql/create_user"

check_user_url = "http://127.0.0.1:5000/pgsql/check_user"

verify_password_url = "http://127.0.0.1:5000/pgsql/verify_password"

get_user_password_url = "http://127.0.0.1:5001/pgsql/get_user_password"

update_user_password_url = "http://127.0.0.1:5000/pgsql/update_user_password"

get_user_token_url = "http://127.0.0.1:5000/pgsql/get_user_token"

delete_user_url = "http://127.0.0.1:5000/pgsql/delete_user"

"""


data_recover = {"username": "abhi" ,"token" : "JsflShSDl2" , "new_password": "1235" , "confirm_password" : "1235"}





"""


data_create_user = {"username": "abhi12" ,"password" : "1235"}
data_check_user = {"username": "abhi7"}
data_verify_password = {"hashed_password" : "$2b$12$PdArGSFvingts6wH9EfbcOzKbTEgoE1jIrbpsqvOCktgYhZn1Ls6W" , "passed_password" : "1235"}
user_password = {"username": "abhi12"}
update_data = {"username": "abhi7" ,"new_password" : "1235"}
data_user_token = {"username": "abhi11"}
delete_user_data = {"username": "abhi7"}


"""


"""

data_signup = {"username": "abhi27" ,"password" : "Qwerty@8503001887" , "confirm_password": "Qwerty@8503001887" }  #JsflShSDl2  token for the user

response_signup = requests.post(signup_url ,json = data_signup)


print("signup json")
print(response_signup.status_code)
print(response_signup.json())

print("end") 

"""


"""
data_login = {"username": "abhi27" ,"password" : "Qwerty@8503001887"}

response_login = requests.post(login_url, json=data_login)

print(response_login.status_code)
print("login json")
print(response_login.json())
print("end")


access_token = response_login.json().get("access_token")
print("access_token : " , access_token)

"""

"""
data_update = {"username": "abhi27" ,"oldPassword" : "Qwerty@8503001887" , "newPassword": "1234" , "confirm_password" : "1234" , "token" : access_token }

response_update = requests.patch(update_url , json = data_update)

print("update json")
print(response_update.status_code)
print(response_update.json())
print("end")

"""



data_login2 = {"username": "abhi27" ,"password" : "1234"}

response_login2 = requests.post(login_url, json=data_login2)

print(response_login2.status_code)
print(response_login2.json())
access_token2 = response_login2.json().get("access_token")




#make the post request to get the user hash 

get_user_token_url = "http://127.0.0.1:5000/pgsql/get_user_token"

user_hash_data = {"username": "abhi27"}
response_get_user_token = requests.post( get_user_token_url , json = user_hash_data)
print("get user token json")
print(response_get_user_token.status_code)
print(response_get_user_token.json())

user_hash = response_get_user_token.json().get("user_hash")
print("user_hash : " , user_hash)  #getting the user hash as none 

print("end")


"""

data_delete =  {"username": "abhi27" ,"userHash" : user_hash , "password": "1234" }

response_delete = requests.post(delete_url ,json = data_delete)

print("delete json")
print(response_delete.status_code)
print(response_delete.json())
print("end")

"""


"""
response_recover = requests.put(recover_url , json = data_recover )
#response_delete = requests.delete(delete_url , json = data_delete)

response_create_user = requests.post(create_user_url, json= data_create_user)
response_check_user = requests.post(check_user_url, json= data_check_user)
response_verify_password = requests.post( verify_password_url , json = data_verify_password)  #error 
response_user_password = requests.post( get_user_password_url , json = user_password)
response_update_user_password = requests.put( update_user_password_url , json = update_data)
response_get_user_token = requests.post( get_user_token_url , json = data_user_token)
response_delete_user = requests.delete( delete_user_url , json = delete_user_data)

"""










"""
print(response_recover.status_code)
print(response_recover.json())


print("-----------------new methods---------------------")


print(response_create_user.status_code)
print(response_create_user.json())


print(response_check_user.status_code)
print(response_check_user.json())





print(response_user_password.status_code)
print(response_user_password.json())


print(response_update_user_password.status_code)
print(response_update_user_password.json())


print(response_get_user_token.status_code)
print(response_get_user_token.json())

print(response_delete_user.status_code)
print(response_delete_user.json())


print(response_verify_password.status_code)
print(response_verify_password.json())

#print(response_delete.status_code)
#print(response_delete.json())


"""
