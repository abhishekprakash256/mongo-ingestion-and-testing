"""
The file to test the login mechanis m of the webiste 
"""

import requests


signup_url = "http://127.0.0.1:5001/auth/signup"

login_url = "http://127.0.0.1:5001/auth/login"

update_url = "http://127.0.0.1:5001/auth/update-password"

recover_url = "http://127.0.0.1:5001/auth/recover"

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






"""


data_create_user = {"username": "abhi12" ,"password" : "1235"}
data_check_user = {"username": "abhi7"}
data_verify_password = {"hashed_password" : "$2b$12$PdArGSFvingts6wH9EfbcOzKbTEgoE1jIrbpsqvOCktgYhZn1Ls6W" , "passed_password" : "1235"}
user_password = {"username": "abhi12"}
update_data = {"username": "abhi7" ,"new_password" : "1235"}
data_user_token = {"username": "abhi11"}
delete_user_data = {"username": "abhi7"}


"""

print("-----------------sign up----------------------")

data_signup = {"username": "abhi27" ,"password" : "Qwerty@8503001887" , "confirm_password": "Qwerty@8503001887" }  #JsflShSDl2  token for the user

response_signup = requests.post(signup_url ,json = data_signup)


print("signup json")
print(response_signup.status_code)
print(response_signup.json())


print("-----------login end------------------")





print("-----------------login ----------------------")
data_login = {"username": "abhi27" ,"password" : "Qwerty@8503001887"}

response_login = requests.post(login_url, json=data_login)

print(response_login.status_code)
print("login json")
print(response_login.json())
print("end")


access_token = response_login.json().get("access_token")
print("access_token : " , access_token)



print("-------------- login end  -----------------")





print("-----------------update user  ----------------------")
data_update = {"username": "abhi27" ,"oldPassword" : "Qwerty@8503001887" , "newPassword": "1234" , "confirm_password" : "1234" , "token" : access_token }

response_update = requests.patch(update_url , json = data_update)


print(response_update.status_code)
print(response_update.json())



print("-------------- update user -----------------")




data_login2 = {"username": "abhi27" ,"password" : "1234"}

response_login2 = requests.post(login_url, json=data_login2)


print("-----------------login start----------------------")

print(response_login2.status_code)
print(response_login2.json())
access_token2 = response_login2.json().get("access_token")

print("-----------login end------------------")


#make the post request to get the user hash 

#from flask url
get_user_token_url = "http://127.0.0.1:5000/pgsql/get_user_token"


print("------------get user token json------")

user_hash_data = {"username": "abhi27"}
response_get_user_token = requests.post( get_user_token_url , json = user_hash_data)
print(response_get_user_token.status_code)
print(response_get_user_token.json())

user_hash = response_get_user_token.json().get("user_token")
print("user token/hash : " , user_hash)  #getting the user hash as none 

print("------------------getting token end-------------------")





print("-----------------recover password----------------------")

data_recover = {"username": "abhi27" ,"token" : user_hash , "newPassword": "1235" , "confirmPassword" : "1235"}


response_recover = requests.post(recover_url , json = data_recover )


print(response_recover.status_code)
print(response_recover.json())

print("-----------------recover password end----------------------")





print("--------------------------delete json---------------------")

#test the user token 

data_delete =  {"username": "abhi27" ,"token" : user_hash , "password": "1235" }

response_delete = requests.post(delete_url ,json = data_delete)

print(response_delete.status_code)

print(response_delete.json())

print("------------------getting end---------------------")













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
